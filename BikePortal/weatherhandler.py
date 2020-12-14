import requests
import json

class WeatherHandler:


    def get_weather_data(self):
        url = 'http://127.0.0.1:5000/forecast'
        weather_request = requests.get(url)
        json_data = weather_request.json()
        print(json_data)
        actual_weather_data= {}#(data for data in json_data)
        return actual_weather_data



