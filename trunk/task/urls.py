#! -*- coding:utf-8 -*-
from django.conf.urls.defaults import *
from getthingsdone.task.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('getthingsdone.task',
    # Example:
    # (r'^getthingsdone/', include('getthingsdone.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^$', task),
    (r'^edit/(\d*)$', edit),
)
