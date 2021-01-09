from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from formApp import views

urlpatterns = [
    url(r'^$',views.form_view,name='form'),
    url('users/',views.users,name='form'),
]
