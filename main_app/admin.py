from django.contrib import admin
from .models import Aftermarket, Car, OilChange

# Register your models here.

admin.site.register(Car)
admin.site.register(OilChange)
admin.site.register(Aftermarket)