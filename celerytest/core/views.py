# Create your views here.
from django.http import HttpResponse

from celerytest.core.models import Counter
from celerytest.core.tasks import celerizied_get, celerizied_increment


def get_counter_name(func):
    def wrapper(request, *args, **kwargs):
        try:
            counter_name = request.GET["counter"]
        except IndexError:
            counter_name = "default"
        return func(request, counter_name, *args,**kwargs)
    return wrapper

def get_counter(func):
    def wrapper(request, counter_name, *args, **kwargs):
        try:
            counter = Counter.objects.get(name=counter_name)
        except Counter.DoesNotExist:
            counter = Counter(name=counter_name,value=0)
        return func(request, counter, *args,**kwargs)
    return wrapper

@get_counter_name
@get_counter
def increment_view(request, counter):
    counter.value += 1
    counter.save()
    return HttpResponse("OK")

@get_counter_name
def delayed_increment_view(request, counter_name):
    result = celerizied_increment.delay(counter_name)
#    result.get() # let's wait for response
#    celerizied_get.delay("http://127.0.0.1:8000/add?%s=dupa" % counter_name)
    return HttpResponse("OK")


@get_counter_name
@get_counter
def value_view(request, counter):
    return HttpResponse("%s" % counter.value)


@get_counter_name
@get_counter
def reset_view(request, counter):
    counter.delete()
    return HttpResponse("OK")
