from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path("flights/", views.flights, name="flights"),
    path("about/", views.flights, name="about"),
    path("<int:flight_id>", views.flight, name="flight")
    #path("<int:flight_id>/book", views.book, name="book")
]
