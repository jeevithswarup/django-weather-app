from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf  import settings

def get_weather_details(request):
    city=request.GET.get('city')


    if not city:
        return JsonResponse(
            {"error": "city name is requried"},
            status=400
        )
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.WEATHER_API_KEY}"


    response=requests.get(url)
    
    if response.status_code != 200:
        return JsonResponse(
            {"error":"City is not found"},status=404
        )
    
    data=response.json()


    fetch_data={
        
        "city_name":data["name"],
        "temperature":data["main"]["temp"],
        "humidity":data["main"]["humidity"],
        "weather":data["weather"][0]["description"],
         "wind_speed":data["wind"]["speed"]
    }
    return JsonResponse(fetch_data)

def home(request):
    return render(request,'home.html')

