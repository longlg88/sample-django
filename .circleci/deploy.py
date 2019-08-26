#!/usr/bin/python3

from fabric.api import env, run, cd, task

debug = False

"""
Fabric deploy script

This is a Fabric (python 2.7) deployment script to be used by CircleCI to
deploy this project automatically to either production or staging.
"""

if debug:
    import paramiko
    paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)

env.venv_name = 'sample-django'
env.path = '~/sample-django'
env.user = 'admin'


@task
def production():
    env.branch = 'master'
    env.hosts = ['timmyomahony.com', ]


@task
def staging():
    env.branch = 'develop'
    env.hosts = ['timmyomahony.com', ]


@task
def venv(cmd):
    run('workon {0} && {1}'.format(env.venv_name, cmd))


@task
def deploy():
    with cd(env.path):
        run('git pull origin {0}'.format(env.branch))
        venv('pip3 install -r requirements.txt')
        venv('python3 manage.py migrate')
        venv('python3 manage.py collectstatic --noinput')
        run('supervisorctl reread')
        run('supervisorctl update')
        run('supervisorctl restart sample-django')