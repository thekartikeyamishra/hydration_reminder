import os
import geocoder 
from dotenv import load_dotenv

load_dotenv() 

def get_current_location():
    try:
        g = geocoder.ip('me')
        return g.latlng
    except Exception as e:  
        print(f"Error getting location: {e}")
        return None  

if __name__ == "__main__":  
    location = get_current_location()
    if location:
        print(f"Your coordinates: {location}")
    else:
        print("Location could not be determined.")
