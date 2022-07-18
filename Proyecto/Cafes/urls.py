from django.contrib import admin
from django.urls import path, include
from . import views

urlpattern=[
    path('', views.inicio, name='inicio'),
    
]