from django.conf.urls.defaults import *
from getthingsdone.settings import STATIC_PATH
from getthingsdone.users.views import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^getthingsdone/', include('getthingsdone.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^$', include('getthingsdone.users.urls')),
    (r'^task/', include('getthingsdone.task.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':STATIC_PATH}),
    (r'^login/$', login),
    (r'^logout/$', logout),
    (r'^register/$', register),
    (r'^checkname/$', check_name),
)
