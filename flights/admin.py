from django.contrib import admin
from .models import Airport, Country, Flight

admin.site.register(Airport)
admin.site.register(Country)
admin.site.register(Flight)
