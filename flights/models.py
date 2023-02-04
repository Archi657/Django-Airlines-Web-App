from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self) :
        return f"{self.name}"

class Airport(models.Model):
    name = models.CharField(max_length=55)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="airports")

    def __str__(self):
        return f"{self.name} ({self.country})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")

    departure = models.DateTimeField(auto_now=True) # save it every time, allowing to update the hour.
    arrival = models.DateTimeField(auto_now=True) 

    airplane = models.ForeignKey('Airplane', on_delete=models.SET_NULL, null=True, related_name="flights",blank=True)

    def __str__(self):
        return f"{self.origin} to {self.destination}"

class Airplane(models.Model):
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE, related_name="plane", primary_key=True)

    a1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seata1", blank=True)
    a2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seata2", blank=True)
    a3 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seata3", blank=True)
    a4 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seata4", blank=True)
    b1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seatb1", blank=True)
    b2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seatb2", blank=True)
    b3 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seatb3", blank=True)
    b4 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seatb4", blank=True)
    c1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seatc1", blank=True)
    c2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seatc2", blank=True)
    c3 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seatc3", blank=True)
    c4 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="seatc4", blank=True)

    def __str__(self):
        return f"From : {self.flight.origin} to {self.flight.destination}"

