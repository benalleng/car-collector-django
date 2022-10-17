from django.urls import path
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
from . import views


urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('cars/', views.cars_index),
]