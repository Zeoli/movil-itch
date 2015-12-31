from django.conf.urls import patterns, include, url
from django.contrib import admin
import usuario.urls
import html5_appcache

html5_appcache.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(usuario.urls)),
    url('^', include('html5_appcache.urls')),
)
