#!/usr/bin/python
#coding: utf-8
"""
This is a setup script for LD recruitment task by Łukasz Biernot.
"""

from distutils.core import setup


setup(
    name="LDRecruitmentŁB",
    author="Łukasz Biernot",
    author_email="lukasz.biernot@gmail.com",
    description="WebApp to monitor battery and WiFi",
    long_description="Based on Django, Tornado and DBus allows continuous "
    "monitoring of battery state and available wireless networks in browser",
    classifiers=[
        "Development Status :: 0.1 - Alpha",
        "License :: OSI Approved :: LGPLv3",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7"
    ],
    packages=[
        "ld_recruitment_lb",
        "ld_recruitment_lb.common",
        "ld_recruitment_lb.battery",
        "ld_recruitment_lb.wifi"
    ],
    package_dir={"ld_recruitment_lb": "lib"},
    package_data={
        "ld_recruitment_lb.common": [
            "templates/common/*.html",
            "static/common/css/*.css",
            "static/common/img/*.png",
            "static/common/js/*.js"
        ],
        "ld_recruitment_lb.battery": [
            "templates/battery/*.html",
            "static/battery/img/*.png"
        ],
        "ld_recruitment_lb.wifi": [
            "templates/wifi/*.html",
            "static/wifi/img/*.png"
        ]
    },
    scripts=["scripts/ld_recruitment_lb_run"],
    requires=[
        "django",
        "tornado",
        "python_dbusx"
    ],
    license="LGPLv3",
    version="0.0.1",
)