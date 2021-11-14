from django.urls import path

from . import views

urlpatterns =[
    path("" , views.home, name="home"),
    path("about/", views.about, name="about"),
    path("flights/", views.flights, name="flights"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
]