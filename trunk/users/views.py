#! -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from getthingsdone.settings import HOST
from datetime import datetime, timedelta
from getthingsdone.users.models import *
from getthingsdone.project.models import *
from getthingsdone.place.models import *
from getthingsdone.task.models import *

# Create your views here.

def index(request):
    name = request.session.get("user")
    if name:
        return HttpResponseRedirect(reverse("getthingsdone.task.views.task"))
    return render_to_response("users/index.html", {"HOST":HOST})

def register(request):
    name = request.session.get("user")
    if name:
        return HttpResponseRedirect(reverse("getthingsdone.task.views.task"))

    username = request.POST.get("username")

    user = User.objects.filter(username=username)
    if user:
        REG_INFO = {"REG_INFO" : "重复的用户名,请重新注册."}
        REG_INFO["HOST"] = HOST
        return render_to_response("users/index.html", REG_INFO)

    password = request.POST.get("password")
    email = request.POST.get("email")
    sex = 2
    status = 0
    reg_time = datetime.now()
    newuser = User(username=username, password=password, email=email, sex=sex, reg_date=reg_time, status=status)
    newuser.save()
    
    project = Project(owner=newuser, name="日常事务", note="管理自己的日常事务",\
                        priority=1, color="black", create_date = reg_time, status=0)
    project.save()

    place = Place(owner=newuser, name="家中", note="在家中完成的事务", create_date = reg_time, status=0)
    place.save()

    task = Task(owner=newuser, name="完善你的个人信息", note="这是系统自动生成的任务,你可以进行修改,删除",\
                    place=place, project=project, color="black", start_date=reg_time, deadline=reg_time+timedelta(days=3), \
                    remind_date = reg_time + timedelta(days=3) - timedelta(hours= 2), remind_type = "email", \
                    repeat_date = datetime(1900,1,1), repeat_freq = 4, status = 0)
    task.save()
    info = {"INFO" : "注册成功."}
    info['HOST'] = HOST
    return HttpResponseRedirect(reverse('getthingsdone.users.views.index'))

def login(request):
    name = request.session.get("user")
    if name:
        return HttpResponseRedirect(reverse("getthingsdone.task.views.task"))

    username = request.POST.get("user")
    password = request.POST.get("pass")

    user = User.objects.filter(username=username).filter(password=password)
    if user:
        request.session['user'] = str(user[0].id)
        return HttpResponseRedirect(reverse("getthingsdone.task.views.task"))
    else:
        error_info = {"INFO" : "账号错误,请检查输入."}
        error_info["HOST"] = HOST
        return render_to_response("users/index.html", error_info)

def logout(request):
    if request.session.get("user"):
        del request.session['user']
    return HttpResponseRedirect(reverse("getthingsdone.users.views.index"))

def check_name(request):
    name = request.POST.get("username")
    if name is None:
        return HttpResponseRedirect(reverse("getthingsdone.users.views.index"))
    user = User.objects.filter(username = name)
    response = HttpResponse()
    if user:
        response.write("ERROR") #重复的用户名
    else:
        response.write("OK") # OK
    return response
