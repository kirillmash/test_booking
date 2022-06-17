from django.contrib import admin

from reservation.models import Reservation, Rental

admin.site.register(Reservation)
admin.site.register(Rental)
