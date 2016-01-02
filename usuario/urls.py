from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',

    url(r'^$', views.Main),
    url(r'^register/$', views.Create),
)