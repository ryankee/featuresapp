FEATURES APP
============

Manage, track, and organize projects around features. View the [demo](http://featuresapp.com/demo/) to see where we are.

INSTALLATION
------------

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

Our installation process:

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
