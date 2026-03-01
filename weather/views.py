from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf  import settings
from datetime import datetime
def get_weather_details(request):
    city=request.GET.get('city_name')


    if not city:
        return render(request,'home.html',
            {"error": "city name is requried"},
            status=400
        )
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.WEATHER_API_KEY}"


    response=requests.get(url)
    
    if response.status_code != 200:
        return render(request,'home.html',
            {"error":"City is not found"},status=404
        )
    
    data=response.json()
    rain = 0
    if "rain" in data:
     rain = data["rain"].get("1h", data["rain"].get("3h", 0))


    image_url = None
    unsplash_url = "https://api.unsplash.com/search/photos"

    image_params = {
        "query": f"{city} city landscape",
        "client_id": settings.UNSPLASH_ACCESS_KEY,
        "orientation": "landscape"
    }

    image_response = requests.get(unsplash_url, params=image_params)

    if image_response.status_code == 200:
        image_data = image_response.json()
        if image_data["results"]:
            image_url = image_data["results"][0]["urls"]["regular"]
    fetch_data={
        "city_name":data["name"],
        "temperature":data["main"]["temp"],
        "humidity":data["main"]["humidity"],
        "weather":data["weather"][0]["description"],
        "wind_speed":data["wind"]["speed"],
        "pressure":data["main"]["pressure"],
        "visibility":data.get("visibility",0)/1000,
        "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]),
        "sunset": datetime.fromtimestamp(data["sys"]["sunset"]),
        "rain": rain,
        "background_image": image_url,

    }
    return render(request,'home.html',fetch_data)

 
