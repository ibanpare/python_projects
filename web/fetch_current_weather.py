"""
Gets the current weather for a given city, trying to locate the user automatically

TO DOs:
- call should be converted to lat/lng for inferred location
- some error management
"""

import os
import requests

PROXY = {"https": "185.156.172.122:3128"}

#gets user IP
IP_URL = "https://httpbin.org/ip"
ip_res = requests.get(IP_URL, proxies=PROXY)
user_ip = ip_res.json()['origin']

#locates user with ipstack API
ipstack_url = f"http://api.ipstack.com/{user_ip}?access_key={os.environ['IPSTACK_API_KEY']}&format=1"
ipstack_res = requests.get(ipstack_url)
user_latitude = ipstack_res.json()['latitude']
user_longitude = ipstack_res.json()['longitude']
city = ipstack_res.json()['city']
state = ipstack_res.json()['region_name']
country = ipstack_res.json()['country_code']

def weather_api_call(city, state, country):
    """
    Manages US vs rest of the world Open Weather API calls, by city
    """
    if country == "US":
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={os.environ['OPENWEATHER_API_KEY']}&units=metric"
        return api_url
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={os.environ['OPENWEATHER_API_KEY']}&units=metric"
    return api_url

def gets_weather(api_url):
    """
    This call Open Weather API by city and prints results
    """

    res = requests.get(api_url)
    data = res.json()

    print()
    print(f"The weather forecast for {city}, {country} is:")
    print(f"{data['weather'][0]['description']}")
    print()
    print("The temperature now is:")
    print(f"{data['main']['temp']} degrees Celsius.")
    print("Which feels like:")
    print(f"{data['main']['feels_like']} degrees Celsius.")


print()
print(f"Your IP address is {user_ip}")
print(f"It looks like you may be in {city}, {state}, {country}")

if input("Is that correct? Should I fetch weather for there? (Y or N) ").lower() == "y":
    gets_weather(weather_api_call(city,state,country))
else:
    print("Wrong?")
    print("Ok, you tell me where you are then.")

    city = input("Please enter the name of the city: ")
    #ISO 3166 country codes are supported
    country = input("Please input your country code (for example FR for France): ")
    if country == "US":
        state = input("Please input your state code (for example VT for Vermont): ")
    gets_weather(weather_api_call(city,state,country))
