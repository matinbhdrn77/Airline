from flights.models import Flight, Airport, Passenger
from django.contrib import admin

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
