from fabric.api import env, run, sudo, put, local, get
from fabric.context_managers import prefix, cd
from fabric.contrib.files import upload_template
from fabric.contrib.project import rsync_project
from fabric.operations import reboot
import os

RSYNC_EXCLUDE = ['*.pyc','/.idea','/bin','/develop-eggs','/eggs', '/parts','/.installed.cfg', '/downloads', '/bootstrap.py','/*.egg-info','/data.db']

def _get_proj_dir():
    return os.path.dirname(env.real_fabfile)

def rsync():
    rsync_project(remote_dir='wsgiapp', local_dir="%s/"%_get_proj_dir(), delete=True, exclude=RSYNC_EXCLUDE)

def make():
    with cd('wsgiapp'):
        run('make')

def make_clean():
    with cd('wsgiapp'):
        run('make clean')


def runserver():
    with cd('wsgiapp'):
        run('./bin/gunicorn celetytest.wsgi:application')
