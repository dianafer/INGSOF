from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.models import *
urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),
    (r'^login/$', 'django.contrib.auth.views.login'),
)

