#! -*- coding:utf-8 -*-
#! -*- coding:utf-8 -*-
from django.db import models
from getthingsdone.users.models import *

# Create your models here.
class Place(models.Model):
    owner = models.ForeignKey(User, verbose_name = "the userr the places belong to ")
    name = models.CharField(max_length = 50)
    note = models.CharField(max_length = 50)
    create_date = models.DateField()
    status = models.IntegerField()  #0 : ok, 1:delted, others reseved for future

    def __unicode__(self):
        return "Place: %s(%s)" % (self.name, self.owner)



