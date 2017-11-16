
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


# Create your models here.
class Car(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    make = models.CharField(max_length=140)
    tipe = models.CharField(max_length =140)
    year = models.CharField(max_length =140)
    colour = models.CharField(max_length=140)
    #price = models.DecimalFiel(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    create = models.DateTimeField(auto_now = True)


    def __str__(self):
        return str(self.make)
