from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$',views.help,name='help'),
    url('index/',views.index,name='index'),
    url('Users/',views.user,name='user'),
]
