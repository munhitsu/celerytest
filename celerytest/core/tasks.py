import urllib2
from celery.task import task
from celerytest.core.models import Counter

@task
def celerizied_get(url):
    data_socket = urllib2.urlopen(url)
    data = data_socket.read()

@task
def celerizied_increment(counter_name):
    try:
        counter = Counter.objects.get(name=counter_name)
    except Counter.DoesNotExist:
        counter = Counter(name=counter_name,value=0)
    counter.value += 1
    counter.save()
