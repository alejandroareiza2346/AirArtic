"""AirArctic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'BookFlight/exploreTrip.html')  # Render the original exploreTrip.html template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Flight.urls')),
    path('api/', include('Member.urls')),
    path('api/', include('Trip.urls')),
    path('api/', include('Explore.urls')),
    path('', home, name='home'),  # Update the root URL to use the original home view
]
