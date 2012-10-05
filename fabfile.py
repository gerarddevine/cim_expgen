from fabric.api import *
from os import path


env.user = 'root'
env.shell = "/bin/bash -c"
env.hosts = ['server_ip',] # these are defined in your /.ssh/config Host host1, Host host2, etc.
env.password = "" # at lease for me it's easier to keep my password in the fabfile


### Local tasks
def commit(message):
    local('git add .') 
    _commit = "git commit -a -m '{0}'".format(message)
    local(_commit)
    local('git push origin master')


### Server tasks
def reload_server():
    sudo('invoke-rc.d apache2 reload')


def deploy():
    with cd('/home/djangoapp'):
        sudo('git pull')
    
    reload_server


#-------------------------------------------------------------
# New code
#
#-------------------------------------------------------------

def prepare_deployment():
    local('echo "Preparing deployment......."')
    local('git status')
    local('git add .')
    local('git commit') 
    local('git push origin master')  # Push master to github repository
'''
