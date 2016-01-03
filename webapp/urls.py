from django.conf.urls import patterns, include, url
from django.contrib import admin
import usuario.urls
import producto.urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(usuario.urls)),
    url(r'^', include(producto.urls))
)
