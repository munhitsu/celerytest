from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^add$', 'celerytest.core.views.increment_view', name='increment_view'),
    url(r'^longadd$', 'celerytest.core.views.delayed_increment_view', name='delayed_increment_view'),
    url(r'^value$', 'celerytest.core.views.value_view', name='value_view'),
    url(r'^reset$', 'celerytest.core.views.reset_view', name='reset_view'),
)
