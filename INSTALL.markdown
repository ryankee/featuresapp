INSTALLATION
============

FeaturesApp is built on Django and so any django set up will work. Ours 
currently looks like this:

- Ubuntu 10.10
- PostgreSQL 8.4.7 postgresql-client pgadmin3 python-psycopg2
- Nginx 0.7.67
- python-setuptools python-dev build-essential
- pip 0.8.3
- virtualenv 1.5.2
- Django 1.3
- gunicorn 0.12.1
- rsync 3.0.7

Our installation process for production servers:

    $ sudo aptitude update
    $ sudo aptitude install postgresql postgresql-client pgadmin3
    $ sudo passwd postgres
    $ su postgres
    $ psql -d template1
    # ALTER USER postgres WITH PASSWORD 'password';
    # \q
    $ exit
    $ sudo aptitude install nginx
    $ sudo aptitude install python-setuptools python-dev build-essential
    $ sudo easy_install -U pip
    $ sudo pip install -U virtualenv
    $ mkdir -p /srv/python-environments
    $ cd /srv/python-environments
    $ virtualenv --no-site-packages --distribute featuresapp
    $ source featuresapp/bin/activate
    $ sudo apt-get build-dep python-psycopg2
    $ sudo pip install Django -E featuresapp
    $ sudo pip install gunicorn -E featuresapp
    $ sudo aptitude install rysnc

Once the production server is set up we do the following:

    $ git clone git://github.com/bytecollective/featuresapp.git
    $ cd featuresapp
    $ vim private_info.py
    def private_env():
        ''' Set the private env data (No need to call) '''
        env.user = 'username'
        env.password = 'password'
        env.dest = 'destination'
        env.hosts = ['host']
        return env
    $ cd featuresapp
    $ vim production_settings.py
    from settings import *

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'databasename',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': '',
            'PORT': '',
        }
    }
    $ fab fresh_deploy

At this point featuresapp should be running on the server.
