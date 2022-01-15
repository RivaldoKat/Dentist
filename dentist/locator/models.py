from django.db import models

# Create your models here.

class Location(models.Model):
    store_name = models.CharField(max_length=30, default='Store name')
    name  = models.CharField(max_length=250)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
