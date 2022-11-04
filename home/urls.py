# Lines 3 to 9 Credit Code Institute, Boutique Ado

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
