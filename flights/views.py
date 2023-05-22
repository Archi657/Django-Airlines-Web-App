from django.shortcuts import render
from django.http import HttpResponse
from .models import Country, Airport, Flight

def home(request):
    countries = Country.objects.all()
    flights = Flight.objects.all()
    return render(request, 'home.html', {'countries':countries, 'flights':flights})

def flights(request):
    return render(request,"flights/flights.html",{
        "flights": Flight.objects.all(),
        'countries': Country.objects.all() 
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight" : flight,
        "passengers": flight.passengers.all(),
        #"non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

#def about(request):
#    return render(request, 'aboutus.html')



#def book(request, flight_id):
#    if request.method == "POST":
#        flight = Flight.objects.get(pk=flight_id)
#        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
#        passenger.flights.add(flight)
#        return HttpResponseRedirect(reverse("flight", args=(flight.id)))
