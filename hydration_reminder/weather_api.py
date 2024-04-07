import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_temperature(city):
    params = {
        'q': city, 
        'appid': os.getenv('OPENWEATHERMAP_API_KEY'),
        'units': 'metric'  
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['main']['temp']
    else:
        return None  
