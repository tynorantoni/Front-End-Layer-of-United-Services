import requests
import json

class CyclingDataHandler:


    def get_all_cycling_data(self,city):
        url = f'http://127.0.0.1:5000/statistic&city={city}'
        all_cycling_data_request = requests.get(url)
        json_data = all_cycling_data_request.json()
        print(json_data)
        actual_weather_data= {}#(data for data in json_data)
        return actual_weather_data


    def get_data_for_charts(self,city, startdate, enddate):
        url = f'http://127.0.0.1:5000/city={city}&startdate={startdate}&enddate={enddate}'
        chart_cycling_data_request = requests.get(url)
        json_data = chart_cycling_data_request.json()
        print(json_data)
        actual_weather_data= {}#(data for data in json_data)
        return actual_weather_data


    def get_data_for_statistics(self,city, startdate, enddate):
        url = f'http://127.0.0.1:5000/statistic&city={city}&startdate={startdate}&enddate={enddate}'
        chart_cycling_data_request = requests.get(url)
        json_data = chart_cycling_data_request.json()
        print(json_data)
        actual_weather_data= {}#(data for data in json_data)
        return actual_weather_data

