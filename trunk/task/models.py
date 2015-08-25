#!-*- coding: utf-8 -*-
from django.db import models
from getthingsdone.place.models import *
from getthingsdone.project.models import *

# Create your models here.

class Task(models.Model):
    owner = models.ForeignKey(User, verbose_name = "The user this task belongs to")
    name = models.CharField(max_length = 100)
    note = models.TextField()
    place = models.ForeignKey(Place, verbose_name = "The Place to complete the task")
    project = models.ForeignKey(Project, verbose_name = "The project this task belongs to")
    color = models.CharField(max_length = 50)
    start_date = models.DateField()     # 任务的创建时间
    deadline = models.DateField()       #任务的截止日期
    remind_date = models.DateField()    # 系统提醒时间
    remind_type = models.CharField(max_length = 50) # 系统提醒方式
    repeat_date = models.DateField() # 系统提醒时间, 1900, 1,1  means no reaminder, 
    repeat_freq = models.IntegerField()
    # 系统提醒频率,0:everyday, 1, every week, 2, every month, 3, every year , 4, none
    status = models.IntegerField()  #0, not finished, 1: finished, 2:deleted 

    def __unicode__(self):
        return "Task: %s(%s) " % (self.name, self.owner)
