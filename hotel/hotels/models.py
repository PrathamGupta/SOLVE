# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible


from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Register(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    hotel = models.BooleanField(default=False)
    def __str__(self):
        return self.first_name

@python_2_unicode_compatible
class Card(models.Model):
    hotel_name = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)    
    date = models.DateField()
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.hotel_name