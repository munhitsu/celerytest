from django.db import models

# Create your models here.

class Counter(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, default="")
    value = models.PositiveIntegerField(default=0)
    def __unicode__(self):
        return u'%s: %s' % (self.name, self.value)
