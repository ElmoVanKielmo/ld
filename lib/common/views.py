from django.shortcuts import render_to_response


def index(request):
    context = {
        "project_name": "Battery and WiFi",
        "sections": (
            ("Home", "common/home.html"),
            ("Battery", "battery/battery.html"),
            ("Wireless Networks", "wifi/wifi.html"),
            ("Credits", "common/credits.html")
        )
    }
    return render_to_response("common/index.html", context)
