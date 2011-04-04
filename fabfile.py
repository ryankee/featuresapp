from fabric.api import *
from private_info import *

private_env()

def deploy():
    local('rsync -r . {0}@{1}:/opt/featuresapp.com/'.format(env.user, env.hosts[0]))
    configure_upstart()
    restart_gunicorn()
    configure_nginx()
    restart_nginx()

def configure_upstart():
    sudo('cp {0}/deploy/upstart/gunicorn_featuresapp.conf /etc/init/'.format(env.dest))

def restart_gunicorn():
    sudo('service gunicorn_featuresapp stop')
    sudo('service gunicorn_featuresapp start')

def configure_nginx():
    sudo('cp {0}/deploy/nginx/featuresapp.com /etc/nginx/sites-available/featuresapp.com'.format(env.dest))

def restart_nginx():
    sudo('/etc/init.d/nginx stop')
    sudo('/etc/init.d/nginx start')
