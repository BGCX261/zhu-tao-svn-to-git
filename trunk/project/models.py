#! -*- coding:utf-8 -*-
from django.db import models
from getthingsdone.users.models import *

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(User, verbose_name="owner of the project")
    name = models.CharField(max_length = 50)
    note = models.CharField(max_length = 50)
    priority = models.IntegerField()    #0:low, 1: middle, 2:high
    color = models.CharField(max_length = 50) 
    create_date = models.DateField()
    status = models.IntegerField()  #0 for ok, 1 for delete  

    def __unicode__(self):
        return "Project: %s(%s)" % (self.name, self.owner)

