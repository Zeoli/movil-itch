from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',

    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^edit/perfil/$', views.ProfileEdit),
    url(r'^register/$', views.Create),
)