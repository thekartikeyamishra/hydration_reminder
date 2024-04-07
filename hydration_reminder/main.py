import time

from config import HYDRATION_REMINDER_INTERVAL
from location_tracker import get_current_location
from weather_api import get_temperature
from hydration_calculator import calculate_water_intake
from notifier import show_reminder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.animation import Animation


Builder.load_file('hydration_app.kv') 

class HydrationApp(App):
    def build(self):
        self.ui = HydrationUI()  
        return self.ui
    
class HydrationUI(BoxLayout):  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.temperature_label = self.ids.temperature_label
        self.intake_label = self.ids.intake_label

    def update_hydration_info(self):
        
        try:  
            location = get_current_location()
            if location:
                city = location[1]
                temperature = get_temperature(city)

                if temperature:
                    water_intake = calculate_water_intake(temperature)
                    if water_intake > 0:
                        self.temperature_label.text = f"Current Temperature: {temperature:.1f}°C"  
                        self.intake_label.text = f"Water Intake Recommendation: {water_intake:.2f} liters"
                    else:
                        self.temperature_label.text = f"Current Temperature: {temperature:.1f}°C"
                        self.intake_label.text = "No need to hydrate extra today"
                else:
                   
                    self.temperature_label.text = "Cannot get temperature"
                    self.intake_label.text = ""  
            else:
               
                self.display_error("Location could not be determined")

        except Exception as e: 
            self.display_error(f"Unexpected error: {str(e)}") 

            def display_error(self, message):
                self.temperature_label.text = ""  
                self.intake_label.text = ""
                self.error_label.text = message 
                anim = Animation(opacity=0, duration=2) 
                    



    
def hydration_check():
    location = get_current_location()
    city = location[1]  
    temperature = get_temperature(city)

    if temperature:
        water_intake = calculate_water_intake(temperature)
        if water_intake > 0:
            message = f"Drink {water_intake:.2f} liters of water!"
            show_reminder(message)

if __name__ == "__main__":
    HydrationApp().run()
