from django.contrib import admin
from .models import Airport, Country, Flight, Airplane

admin.site.register(Airport)
admin.site.register(Airplane)
admin.site.register(Country)
admin.site.register(Flight)
