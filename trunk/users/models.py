#! -*- coding:utf-8 -*-
from django.db import models
from getthingsdone.place.models import *

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    sex = models.IntegerField() #0 for male, 1 for female, 2 for others
    reg_date = models.DateField()
    status = models.IntegerField()  #0 for ok, 1 for block

    def __unicode__(self):
        return "User: "+self.username
