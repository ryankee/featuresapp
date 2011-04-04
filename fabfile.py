from fabric.api import *
from private_info import *

private_env()

def deploy():
    ''' Deploy featuresapp to featuresapp.com/demo/ '''
    update_files()
    configure_upstart()
    restart_gunicorn()
    configure_nginx()
    restart_nginx()

def update_files():
    ''' Update the files for featuresapp.com/demo/ '''
    local('rsync -r . {0}@{1}:/opt/featuresapp.com/'.format(env.user, env.hosts[0]))

def configure_upstart():
    ''' Copy upstart conf files to /etc/init/ '''
    sudo('cp {0}/deploy/upstart/gunicorn_featuresapp.conf /etc/init/'.format(env.dest))

def restart_gunicorn():
    ''' Stop and start gunicorn_featuresapp '''
    stop_gunicorn()
    start_gunicorn()

def stop_gunicorn():
    ''' Stop gunicorn_featuresapp '''
    sudo('service gunicorn_featuresapp stop')

def start_gunicorn():
    ''' Start gunicorn_featuresapp '''
    sudo('service gunicorn_featuresapp start')

def configure_nginx():
    ''' Copy nginx conf file to /etc/nginx/sites-available/ '''
    sudo('cp {0}/deploy/nginx/featuresapp.com /etc/nginx/sites-available/featuresapp.com'.format(env.dest))

def restart_nginx():
    ''' Stop and start nginx '''
    stop_nginx()
    start_nginx()

def stop_nginx():
    ''' Stop nginx '''
    sudo('/etc/init.d/nginx stop')

def start_nginx():
    ''' Start nginx '''
    sudo('/etc/init.d/nginx start')
