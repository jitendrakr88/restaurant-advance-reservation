from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(RestaurantStaff)
admin.site.register(Guest)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(ReservedTable)
