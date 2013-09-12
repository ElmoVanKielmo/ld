Web based Battery and WiFi monitor

1. LICENSE AND AUTHOR:
    - This software is distributed under the terms of LGPLv3
    - The author of this software is Łukasz Biernot

2. REQUIREMENTS:
    a) Ubuntu 12.04 or higher
    b) debian packages:
        - python-dev
        - libdbus-1-dev
    c) python libraries:
        - django
        - tornado
        - python-dbusx

3. INSTALLATION:
    * for automated installation run 'sh install_me.sh' - the hard way is here:
    - check if required debian packages are installed
      (e.g. 'dpkg -l | grep python-dev')
    - if some of them are missing or you are not sure, install them with
      'sudo apt-get install python-dev libdbus-1-dev'
    - install required python libraries with
      'sudo pip install -r requirements.txt'
    - if folder 'build' exists remove it with 'rm -rf build'
    - build this project with 'python setup.py build'
    - install it with 'sudo python setup.py install'
    - locate the installation folder
      (probably '/usr/local/lib/python2.7/dist-packages/ld_recruitment_lb/')
      run 'python manage.py collectstatic -l'

4. USAGE:
    - run web server with 'ld_recruitment_lb_run' (use --help for options)
    - start your web browser and enjoy

