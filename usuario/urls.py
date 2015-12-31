from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',

    url(r'^$', views.Login),
    url('^', include('html5_appcache.urls')),
)

import html5_appcache
html5_appcache.autodiscover()