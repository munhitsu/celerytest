celerytest
==========
gunicorn+celery+django+fabric+buildout deployment skeleton


Step 1:
-------
make



Step 2 (run app on localhost)
-----------------------------
./bin/python manage.py runserver
./bin/python manage.py celeryd


Step 3 (deploy on remote host)
-------
fab -H xxxx rsync
fab -H xxxx make


Step 4 (run on remote host)
-------
fab -H xxxx runserver

