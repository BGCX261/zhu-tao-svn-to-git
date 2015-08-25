#! -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from getthingsdone.settings import HOST
from datetime import datetime
from getthingsdone.task.models import *

# Create your views here.

#def index(request):
#    return render_to_response("task/index.html")
#
#def register(request):
#    username = request.POST.get("username")
#    password = request.POST.get("password")
#    email = request.POST.get("email")
#
#    sex = 2
#    status = 0
#    reg_time = datetime.now()
#    newuser = User(username=username, password=password, email=email, sex=sex, reg_date=reg_time, status=status)
#    newuser.save()
#    return HttpResponseRedirect(reverse('getthingsdone.task.views.index'))
#
#def login(request):
#    username = request.POST.get("username")
#    password = request.POST.get("password")
#
#    user = User.objects.filter(username=username).filter(password=password)
#    if user:
#        request.session['user'] = str(user[0].id)
#        return HttpResponseRedirect(reverse("getthingsdone.task.views.task"))
#    else:
#        return HttpResponseRedirect(reverse("getthingsdone.task.views.index"))
#
#    
def task(request):
    userid = request.session.get("user")
    if userid:
        info = {"HOST":HOST}
        current_user = User.objects.get(id=userid)
        tasks = Task.objects.filter(owner=current_user).filter(status="0").order_by("deadline")[:10]
        projects = Project.objects.filter(owner=current_user).filter(status="0").order_by("create_date")[:5]
        places = Place.objects.filter(owner=current_user).filter(status="0").order_by("create_date")
        info['task_list'] = tasks
        info['project_list'] = projects 
        info['place_list'] = places
        return render_to_response("task/task.html", info)
    else:
        return HttpResponseRedirect(reverse('getthingsdone.users.views.index'))
    
def edit(request, task_id):
    uid = request.session.get("user")
    if uid:
        user = User.objects.get(id=uid)
        task = Task.objects.filter(status="0").get(id=task_id)
        projects = Project.objects.filter(status="0").filter(owner=user)
        places = Place.objects.filter(status="0").filter(owner=user)
        min = range(24)
        sec = range(60)
        weekday = ['星期一', '星期二', '星期三','星期四','星期五','星期六','星期天']
        monthday = range(1, 32)
        yearmonth = range(1, 13)
        if task:
            info = {"HOST":HOST}
            info['task'] = task
            info['project_list'] = projects
            info['place_list'] = places
            info['user'] = user
            info['min'] = min
            info['sec'] = sec
            info['weekday'] = weekday
            info['monthday'] = monthday
            info['yearmonth'] = yearmonth 
            return render_to_response("task/edit.html", info)
        else:
            info = {"HOST":HOST}
            info['error'] = "没有此事务!" 
            return render_to_response("task/edit.html", info)
    else:
        return HttpResponseRedirect(reverse('getthingsdone.users.views.index'))
    
def add(request, task_id):
    uid = request.session.get('user')
    if uid:
        name = request.POST.get("name")
        note = request.POST.get("note")
        owner = User.objects.get(id=uid)
        place = request.POST.get('place')
        project = request.POST.get("project")
        start_date = datetime.now()
        deadline = request.POST.get("deadline")
        pass
#中断,task的表设计的有问题,如何提醒?

        if task_id:
            pass

    
