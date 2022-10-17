from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    trim = models.CharField(max_length=100)

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('cars_detail', kwargs={'car_id': self.id})