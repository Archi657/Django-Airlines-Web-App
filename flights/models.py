from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self) :
        return f"{self.name}"

class Airport(models.Model):
    name = models.CharField(max_length=55)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="airports")

    def __str__(self):
        return f"{self.name} from {self.country}"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")

    departure = models.DateTimeField(auto_now=True) # save it every time, allowing to update the hour.
    arrival = models.DateTimeField(auto_now=True) 

class Airplane(models.Model):
    # user foerign key to each seat.
    #seat1a = 