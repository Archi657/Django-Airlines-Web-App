from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Country, Airport, Flight
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    countries = Country.objects.all()
    flights = Flight.objects.all()
    return render(request, 'home.html', {'countries': countries, 'flights': flights})


def flights(request):
    return render(request, "flights/flights.html", {
        "flights": Flight.objects.all(),
        'countries': Country.objects.all() 
    })


def flight(request, flight_id):
    flight_object = Flight.objects.get(pk=flight_id)
    if request.method == "POST":
        print("here")
        if request.user.is_authenticated:
            flight_object.passengers.add(request.user)

    return render(request, "flights/flight.html", {
        "flight": flight_object,
        "passengers": flight_object.passengers.all(),
        # "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'User {username} has been created')
    else:
        form = UserCreationForm()
    ctx = { 'form' : form }
    return render(request, 'register.html', ctx)


def about(request):
    return render(request, 'aboutus.html')

