from datetime import timedelta

from django.shortcuts import render_to_response
from ld_recruitment_lb.dbus_api import DBusApi


BATTERY_STATES = [
    'Unknown',
    'Charging',
    'Discharging',
    'Empty',
    'Fully charged',
    'Pending charge',
    'Pending discharge'
]

BATTERY_ICONS = {
    'charging': [
        'Status-battery-charging-low-icon.png',
        'Status-battery-charging-caution-icon.png',
        'Status-battery-charging-040-icon.png',
        'Status-battery-charging-060-icon.png',
        'Status-battery-charging-080-icon.png',
        'Status-battery-charging-icon.png'
    ],
    'discharging': [
        'Status-battery-low-icon.png',
        'Status-battery-caution-icon.png',
        'Status-battery-040-icon.png',
        'Status-battery-060-icon.png',
        'Status-battery-080-icon.png',
        'Status-battery-100-icon.png'
    ],
    'missing': [
        'Status-battery-missing-icon.png'
    ]
}


def battery(request):
    DBusApi.query = DBusApi.battery
    DBusApi.query_event.set()
    DBusApi.response_event.wait(None)
    properties = DBusApi.response
    DBusApi.response_event.clear()
    context = {'battery': {}}
    if properties is None or not properties[u'IsPresent']:
        context['battery']['is_present'] = False
        context['battery']['icon'] = BATTERY_ICONS['missing'][0]
    else:
        context['battery']['is_present'] = True
        context['battery']['status'] = BATTERY_STATES[properties[u'State']]
        context['battery']['percentage'] = properties[u'Percentage']
        context['battery']['time_to_charge'] = timedelta(
            seconds=properties[u'TimeToFull']
        ) if properties[u'TimeToFull'] > 0 else 'Unknown'
        context['battery']['time_to_discharge'] = timedelta(
            seconds=properties[u'TimeToEmpty']
        ) if properties[u'TimeToEmpty'] > 0 else 'Unknown'
        if properties[u'State'] == 1:
            context['battery']['is_charged'] = True
            icon_type = 'charging'
        else:
            context['battery']['is_charged'] = False
            icon_type = 'discharging'
        context['battery']['icon'] = \
            BATTERY_ICONS[icon_type][int(properties[u'Percentage'] / 20)]
    return render_to_response('battery/battery.html', context)

