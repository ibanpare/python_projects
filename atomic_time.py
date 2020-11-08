"""
This program will get the true atomic time from an atomic time clock on the Internet.
Use any one of the atomic clocks returned by a simple Google search.
"""

import requests
import bs4

res = requests.get("https://www.timeanddate.com/worldclock/other/tai")
soup = bs4.BeautifulSoup(res.text,"lxml")
time = soup.select("#ct")
print(f"The atomic time is now: {time[0].text}")
