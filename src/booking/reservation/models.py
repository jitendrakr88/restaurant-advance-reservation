from datetime import datetime, timedelta

from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Guest(models.Model):
    """Manage the record for guess who booked reservation"""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.name}, {self.phone}'

class RestaurantStaff(models.Model):
    """Manage any restaurants staff. Manager, worker, reception, owner etc"""
    OWNER, MANAGER, STAFF, RECEPTION = 1, 2, 4, 8
    OWNER_MANAGER = OWNER | MANAGER
    STAFF_RECEPTION = STAFF | RECEPTION
    ROLES = (
        (OWNER, _("Owner of the restaurant")),
        (MANAGER, _("Manager of the restaurant")),
        (STAFF, _("Working staff member at the restaurant")),
        (RECEPTION, _("Receptionist of the restaurant")),
        (OWNER_MANAGER, _("Owner as well as Manager of the restaurant")),
        (STAFF_RECEPTION, _("Staff worker as well as receptionist at the restaurant"))
    )
    username = models.SlugField(max_length=25)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=15)
    role = models.IntegerField(choices=ROLES, default=STAFF)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)

    def __str__(self):
        role = RestaurantStaff.get_role_name(self.role)
        return f'{self.name}, {role}, {self.restaurant.name}'

    @staticmethod
    def get_role_name(role_type):
        """Returns actual role type in string fetched using the interger mapping"""
        for role in RestaurantStaff.ROLES:
            if role[0] == role_type:
                return role[1]
        raise Exception("Role type not defined in the Restaurant Staff records")

class Restaurant(models.Model):
    """Restaurant table for holding up various restaurants information in the city"""

    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    opens_at = models.TimeField(null=True) # 24*7
    closes_at = models.TimeField(null=True) # 24*7
    tables = models.PositiveIntegerField()

    address = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}, {self.address}, {self.state}'

class MenuItem(models.Model):
    """Menu items for the restaurants"""
    # TODO Create a bitmap for managing the menu items category.
    slug = models.SlugField(max_length=255, unique=True)
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
    capacity = models.PositiveIntegerField(default=4)
    ocupied = models.BooleanField(default=False)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)

    class Meta:
        unique_together=("number", "restaurant")

    def __str__(self):
        return f'Table number {number} at restaurant={self.restaurant.name}'

class Reservation(models.Model):
    """Manage all the reservations"""
    DEFAULT_DURATION = timedelta(hours=2)

    person = models.ForeignKey(Guest, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    starts = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(default=DEFAULT_DURATION)
    number_of_people = models.PositiveIntegerField(default=4)

    def __str__(self):
        return f'{self.person.name}, Reservation for {self.number_of_people} people, From {self.starts} to {self.ends}'

class ReservedTable(models.Model):
    """records for reseved tables"""
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
