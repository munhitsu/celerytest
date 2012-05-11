from django.contrib import admin
from celerytest.core.models import Counter

admin.site.register(Counter)
