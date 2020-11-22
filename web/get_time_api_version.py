"""
This program will get the true atomic time from an atomic time clock on the Internet.
Use any one of the atomic clocks returned by a simple Google search.

Second version of this, I'll use the http://worldtimeapi.org/ just to practice APIs.
"""

import requests

locations = requests.get("http://worldtimeapi.org/api/timezone/Europe")

#Cleaning up the response text
cities = locations.text
cities = cities.replace('"','')
cities = cities.replace('[','')
cities = cities.replace(']','')
cities = cities.replace('Europe/','')
cities = cities.split(",")

def get_time(place):

    """
    gets time from World Time API
    input required: valid city
    """

    time = requests.get(f"http://worldtimeapi.org/api/timezone/Europe/{place}.txt")
    time = time.text.split("\n")
    print(time[2])

print("Choose a city among the following ones")
for city in cities:
    print(city)

while True:
    choice = input("Pick a city: ")
    if choice in cities:
        get_time(choice)
        break
