from distutils.archive_util import make_archive
from pyexpat import model
from unicodedata import name
from django.shortcuts import render

from django.views import generic

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

cars = [
    Car('Ford', 'F150', 2019),
    Car('Tesla', 'Y', 2019),
    Car('Honda', 'Accord', 2018)
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', {'cars': cars})

# Create your views here.
