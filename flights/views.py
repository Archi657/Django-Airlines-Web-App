from django.shortcuts import render
from django.http import HttpResponse
from .models import Country, Airport, Flight

def home(request):
    countries = Country.objects.all()
    flights = Flight.objects.all()
    return render(request, 'flights/home.html', {'countries':countries, 'flights':flights})

def flights(request):
    return render(request,"flights/flights.html",{
        "flights": Flight.objects.all(),
        'countries': Country.objects.all() 
    })
