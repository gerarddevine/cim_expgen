from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm


env.hosts = ['gdevine@puma.nerc.ac.uk']


def gitupdate():
    local("git add .")
    local("git add -u")
    local("git commit")
    local("git push")


def deploy():
    code_dir = '/home/gdevine/web/prod/cim_expgen'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            print 'YESS, FAILED!!!!!!!!!'
            run("git clone git@github.com:gerarddevine/cim_expgen.git %s" % code_dir)
        else:
            print 'NOOOOO, DIDNT FAIL!!!!!!!!!'
    with cd(code_dir):
        print 'HERE!!!!!!!!!'
        run("pwd")
        run("ls -la")
        run("git pull")
        #run("touch app.wsgi")
