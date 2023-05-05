from django.contrib import admin
from app.models import Person, Pet, Country, Vehicle

admin.site.register(Country)
admin.site.register(Person)
admin.site.register(Pet)
admin.site.register(Vehicle)