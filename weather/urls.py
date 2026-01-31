from django.urls import path
from .views import*

urlpatterns = [
  path('weather_api/',get_weather_details,name="get_weather_details")
]