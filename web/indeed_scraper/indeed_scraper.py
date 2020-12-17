"""
A scraper for indeed.com, Italian version.

It returns the first 100 available search results
for whatever query and location you'd like.
For these results you'll get url, job title and location.
You'll be able to save these info to a file.

specific tasks
- scrape the first 100 available search results
- generalize code to allow searching for different locations and jobs
- pick out info about url, job title and location
- save results to a file
"""

import requests
import bs4

query = str(input("What do you want to search? "))
location = str(input("Where do you want to search? "))
BASE_URL = f"https://it.indeed.com/jobs?q={query}&l={location}"
HOME_URL = "https://it.indeed.com"

#questo si usa per cambiare pagina
#&start=0

res = requests.get(BASE_URL)
soup = bs4.BeautifulSoup(res.content, "lxml")

results = soup.find(id="resultsCol")
jobs = results.find_all("div", class_ = "result")
job_detail = jobs[0].find("h2").find("a")
job_title = job_detail["title"]
job_url = HOME_URL + job_detail["href"]
job_location = jobs[0].find("div", class_= "location")

print(job_title)
print(job_url)
print(job_location.text)
