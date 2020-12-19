"""
Get the current weather for a given zip/postal code. 
*Optional: Try locating the user automatically.*
"""

import requests
import json
import os

city = input("Please enter the name of the city: ")
#ISO 3166 country codes are supported
country = input("Please input your country code (for example FR for France): ")
if country == "US":
	state = input("Please input your state code (for example VT for Vermont): ")
	API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={os.environ['OPENWEATHER_API_KEY']}&units=metric"
else:
	API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={os.environ['OPENWEATHER_API_KEY']}&units=metric"

res = requests.get(API_URL)
data = res.json()

print()
print(f"The weather forecast for {city}, {country} is:")
print(f"{data['weather'][0]['description']}")
print()
print("The temperature now is:")
print(f"{data['main']['temp']} degrees Celsius.")
print("Which feels like:")
print(f"{data['main']['feels_like']} degrees Celsius.")

