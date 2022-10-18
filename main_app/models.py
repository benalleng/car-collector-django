from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Aftermarket(models.Model):
    name = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('aftermarket_detail', kwargs={'pk': self.id})

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    trim = models.CharField(max_length=100)
    aftermarket = models.ManyToManyField(Aftermarket)

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('cars_detail', kwargs={'car_id': self.id})

class OilChange(models.Model):
    CHANGE = (
        ('OIL', 'Oil'),
        ('OIF', 'Oil and Filter'),
        ('OFF', 'Oil, Filter, and Fuses'),
    )

    class Meta:
        ordering = ('-date',)
        
    date = models.DateField('Oil Change Date')
    change = models.CharField(max_length=3, choices=CHANGE, default=CHANGE[0][0])
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_change_display()} on {self.date}'
