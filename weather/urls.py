from django.urls import path
from .views import*

urlpatterns = [
  # path('',home,name="home"),
  path('',get_weather_details,name="get_weather_details")
]