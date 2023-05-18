from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self) :
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"


class Airport(models.Model):
    name = models.CharField(max_length=55)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="airports")

    def __str__(self):
        return f"{self.name} ({self.country})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    departure = models.DateTimeField(auto_now=True)  # save it every time, allowing to update the hour.
    arrival = models.DateTimeField(auto_now=True) 
    airplane = models.ForeignKey('Airplane', on_delete=models.SET_NULL, null=True, related_name="flights", blank=True)
    passengers = models.ManyToManyField(User, related_name="flights")
    
    def __str__(self):
        return f"{self.origin} to {self.destination}"


class Airplane(models.Model):
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE, related_name="flight")
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand} {self.model}"

