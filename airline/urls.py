from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flights.urls'))
]
