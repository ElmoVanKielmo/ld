#!/bin/sh

sudo apt-get install python-dev libdbus-1-dev
sudo pip install -r requirements.txt
rm -rf build
python setup.py build
sudo python setup.py install

sudo python `python <<EOF
from ld_recruitment_lb import manage
import os
print os.path.abspath(manage.__file__)
EOF
` collectstatic -l --noinput
