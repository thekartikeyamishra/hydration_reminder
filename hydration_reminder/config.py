import os
from dotenv import load_dotenv

load_dotenv()  

OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY') 
HYDRATION_REMINDER_INTERVAL = 60
TEMP_THRESHOLD = 30 
WATER_INTAKE_PER_DEGREE = 0.25 
