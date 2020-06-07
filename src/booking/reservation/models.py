from django.db import models
# Create your models here.

class Guest(models.Model):
    """
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}, {self.phone}'

class Restaurant(models.Model):
    """Restaurant table for holding up various restaurants information in the city"""
    slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    opens_at = models.TimeField(null=True)
    closes_at = models.TimeField(null=True)
    tables = models.PositiveIntegerField()

    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}, {self.city}'

class MenuItem(models.Model):
    """Menu items for the restaurants"""
    # TODO Create a bitmap for managing the menu items category.
    slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'restaurant')

    def __str__(self):
        return f'{self.name} at {self.restaurant.name} is priced at {self.price}'

class Table(models.Model):
    """Tables for the restaurants"""
    number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    ocupied = models.BooleanField(default=False)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)

class Reservation(models.Model):
    """Manage all the reservations"""
    person = models.ForeignKey(Guest, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    number_of_people = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.person.name}, Reservation for {self.number_of_people} people, From {self.starts} to {self.ends}'

class ReservedTable(models.Model):
    """records for reseved tables"""
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
