from django.shortcuts import render, HttpResponse
import json
import requests

# Create your views here.
def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=716934bface8a71ae0f2c47453d2329b"
        
        response = requests.get(source.format(city))  # Make the request
        list_of_data = response.json()  # Convert response to JSON
        
        print(list_of_data)  # Debugging purposes

        if isinstance(list_of_data, dict):  # Ensure response is a dictionary
            temperature = list_of_data.get('temp', 'N/A')  # Use `.get()` to avoid KeyError
            
            data = {
                "country_code": str(list_of_data.get('sys', {}).get('country', 'N/A')),
                "coordinate": str(list_of_data.get('coord', {}).get('lon', 'N/A')) + ' ' + str(list_of_data.get('coord', {}).get('lat', 'N/A')),
                "temp": round((list_of_data.get('main', {}).get('temp', 32) - 32) * 5.0 / 9.0, 2),
                "humidity": str(list_of_data.get('main', {}).get('humidity', 'N/A'))
            }
        else:
            data = {}

    else:
        data = {}

    return render(request, "weather.html", data)
