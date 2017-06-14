from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [

    
   
    url(r'^$', views.demo, name='demo'),
    ]