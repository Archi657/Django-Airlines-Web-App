from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Country, Airport, Flight
from django.contrib.auth import authenticate, login, logout


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
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        # "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Wrong Credientals!")
    return render(request, '../templates/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def about(request):
    return render(request, 'aboutus.html')


def book(request, flight_id):
    if request.method == "POST":
        flight_object = Flight.objects.get(pk=flight_id)
        flight_object.passengers.add()
        return HttpResponseRedirect(reverse("flight", args=(flight_object.id)))

