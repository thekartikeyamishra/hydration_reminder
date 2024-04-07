Overview

This Python project provides a user-friendly hydration reminder application built with the Kivy framework. It utilizes location services and weather APIs to offer tailored recommendations and a visually appealing interface.

Features

Location-Based: Fetches the user's current location to determine relevant weather data.
Temperature-Driven Recommendations: Calculates water intake suggestions based on the local temperature.
Customizable UI: Offers a visually pleasing interface designed with Kivy's UI language.
Error Handling: Includes graceful error handling and feedback mechanisms for unexpected situations.
Project Structure

main.py: Core application logic, UI initialization, and hydration update process.
hydration_app.kv: Kivy UI design file, defines the layout and visual elements.
config.py: Stores API keys and configurable parameters.
hydration_calculator.py: Contains the logic for calculating hydration recommendations.
location_tracker.py: Handles retrieving the current user location.
weather_api.py: Interacts with the OpenWeatherMap API to fetch weather data.
notifier.py Implements reminder notifications.
water-drop.png: An image file used in the UI.
BebasNeue-Regular.ttf: Custom font file for styling.
.env: A file to store sensitive API keys (not included in version control).

Dependencies

Python 3.x
Kivy
requests
geocoder
python-dotenv