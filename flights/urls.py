from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path("flights/", views.flights, name="flights"),
    path("about/", views.flights, name="about"),
    path("<int:flight_id>", views.flight, name="flight")
    #path("<int:flight_id>/book", views.book, name="book")
]
