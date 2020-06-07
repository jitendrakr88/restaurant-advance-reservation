from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Restaurant(models.Model):
    """Restaurant table for holding up various restaurants information in the city"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    opens_at = models.TimeField(null=True)
    closes_at = models.TimeField(null=True)

    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

class MenuItem(models.Model):
    """Menu items for the restaurants"""
    # TODO Create a bitmap for managing the menu items category.
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Table(models.Model):
    """Tables for the restaurants"""
    number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    ocupied = models.BooleanField(default=False)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)

