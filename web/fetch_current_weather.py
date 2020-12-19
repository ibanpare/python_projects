"""
Get the current weather for a given zip/postal code. 
*Optional: Try locating the user automatically.*
"""

import requests

API_URL = f"api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}"