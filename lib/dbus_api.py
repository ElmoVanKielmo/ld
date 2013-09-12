from itertools import chain
from threading import Event
from dbusx import Connection, BUS_SYSTEM


class DBusApi(object):

    NM = {
        "service": "org.freedesktop.NetworkManager",
        "path": "/org/freedesktop/NetworkManager",
    }
    NM_INTERFACE = {
        "device": ".".join((NM["service"], "Device")),
        "wireless": ".".join((NM["service"], "Device.Wireless")),
        "access_point": ".".join((NM["service"], "AccessPoint"))
    }

    query = None
    response = None
    query_event = Event()
    response_event = Event()
    shutdown_event = Event()

    @classmethod
    def run_me(cls):
        cls.__bus = Connection(BUS_SYSTEM)
        cls.query_event.clear()
        cls.response_event.clear()
        cls.shutdown_event.clear()
        try:
            while not cls.shutdown_event.wait(1):
                if not cls.query_event.wait(10):
                    continue
                if callable(cls.query):
                    cls.response = cls.query()
                else:
                    cls.response = None
                cls.query = None
                cls.query_event.clear()
                cls.response_event.set()
        finally:
            cls.__bus.close()

    @classmethod
    def battery(cls):
        upower = cls.__bus.proxy(
            "org.freedesktop.UPower",
            "/org/freedesktop/UPower"
        )
        devices = [
            cls.__bus.proxy('org.freedesktop.UPower', device_path)
            for device_path in upower.EnumerateDevices()
        ]
        for device in devices:
            device.Refresh()
            properties = device.GetAll('org.freedesktop.UPower.Device')
            if properties[u'Type'][1] == 2:
                return {key: properties[key][1] for key in properties}
        return None

    @classmethod
    def wifi(cls):
        nm = cls.__bus.proxy(cls.NM["service"], cls.NM["path"])
        devices = [
            cls.__bus.proxy(cls.NM["service"], device_path)
            for device_path in nm.GetDevices()
        ]
        wifi_devices = filter(
            lambda device: device.Get(
                cls.NM_INTERFACE["device"], u"DeviceType"
            )[1] == 2,
            devices
        )
        access_points = [
            {
                u"Interface": device.Get(
                    cls.NM_INTERFACE["device"], u"Interface"
                )[1],
                u"Connected": device.Get(
                    cls.NM_INTERFACE["wireless"], u"ActiveAccessPoint"
                )[1] == access_point.path,
                u"AccessPoint": access_point,

            }
            for device, access_point in chain(
                (
                    device,
                    cls.__bus.proxy(cls.NM["service"], access_point_path)
                )
                for device in wifi_devices
                for access_point_path in device.GetAccessPoints()
            )
        ]
        for access_point in access_points:
            properties = access_point[u"AccessPoint"].GetAll(
                cls.NM_INTERFACE["access_point"]
            )
            access_point.update({key: properties[key][1] for key in properties})
            access_point.pop(u"AccessPoint")
        return access_points













