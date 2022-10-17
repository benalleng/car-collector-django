from distutils.archive_util import make_archive
from pyexpat import model
from unicodedata import name
from django.shortcuts import render

from django.views import generic

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', {'cars': cars})

# Create your views here.
