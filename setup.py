from distutils.core import setup

setup(
    name='celerytest',
    version='0.1',
    packages=['celerytest',],
    url='',
    license='',
    author='munhitsu',
    author_email='mateusz@munhitsu.com',
    description='',
    install_requires=['gevent', 'Gunicorn', 'setproctitle', 'Django', 'django-celery', 'ipython','psycopg2'],
)
