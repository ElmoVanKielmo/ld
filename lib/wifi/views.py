"""
This module contains wifi view
"""


from django.shortcuts import render_to_response
from ld_recruitment_lb.dbus_api import DBusApi


WIFI_ICONS = [
    "no-wifi-networks.png",
    "not-connected.png",
    "connected.png"
]


def wifi(request):
    """
    Ask DBus for wifi info (using api), prepare the context and render
    """
    DBusApi.query = DBusApi.wifi
    DBusApi.query_event.set()
    DBusApi.response_event.wait()
    wifi_props = DBusApi.response
    DBusApi.response_event.clear()
    wifi_props.sort(key=lambda ap: ap[u"Strength"], reverse=True)
    if len(wifi_props) == 0:
        icon_no = 0
    elif len([ap for ap in wifi_props if ap[u"Connected"]]) == 0:
        icon_no = 1
    else:
        icon_no = 2
    context = {
        "wifi": wifi_props,
        "icon": WIFI_ICONS[icon_no]
    }
    return render_to_response("wifi/wifi.html", context)
