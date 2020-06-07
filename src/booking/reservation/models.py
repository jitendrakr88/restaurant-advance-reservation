from django.db import models

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

