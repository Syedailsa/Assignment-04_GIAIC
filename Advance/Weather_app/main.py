import requests
from pprint import pprint

API_key = '2ce2553c3e260ee01d2e23eb00636bb0'

city = input("\nEnter a city you want to know the weather for: ")

base_url = 'https://api.openweathermap.org/data/2.5/weather?appid=' + API_key + '&q=' + city

weather_data = requests.get(base_url).json()

pprint(weather_data)