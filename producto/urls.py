from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',

    url(r'^$', views.Main_view),
    url(r'^producto/([0-9]+)/$', views.GetProducto),
)