"""
A scraper for indeed.com, Italian version.

It returns the first 100 available search results
for whatever query and location you'd like.
For these results you'll get url, job title and location.
You'll be able to save these info to a file.

"""

import csv
import time
import requests
import bs4

QUERY = str(input("What do you want to search? "))
LOCATION = str(input("Where do you want to search? "))
HOME_URL = "https://it.indeed.com"

job_titles = []
job_urls = []
job_locations = []

#Loop through pages, until page 7, to get 100 results

for start in range(0, 70, 10):
    BASE_URL = f"https://it.indeed.com/jobs?q={QUERY}&l={LOCATION}&start={start}"
    res = requests.get(BASE_URL)
    soup = bs4.BeautifulSoup(res.content, "lxml")

    #gets all the jobs of the page
    results = soup.find(id="resultsCol")
    jobs = results.find_all("div", class_ = "result")
    job_details = [jobs[i].find("h2").find("a") for i in range(0, len(jobs))]

    #gets all the job titles out of all the jobs' job details
    current_job_titles = [job_details[i]["title"] for i in range(0, len(job_details))]
    job_titles += current_job_titles

    #gets all the job urls out of all the jobs' job details
    current_job_urls = [HOME_URL + job_details[i]["href"] for i in range(0, len(job_details))]
    job_urls += current_job_urls

    #gets all the locations out of all the jobs
    current_job_locations = [jobs[i].find("div", class_= "location") for i in range(0, len(jobs))]
    #cleans the tag and logic in case it's empty
    for i in range(0, len(current_job_locations)):
        try:
            job_locations.append(current_job_locations[i].text)
        except AttributeError:
            job_locations.append("No Location")

    #a little delay not to get blocked
    time.sleep(0.5)
    print("Fetching data...")

print("Data extracted successfully!")
print(f"You got {len(job_titles)} records.")

#creates csv and header, if user wants
if str(input("Do you want to save these to a csv file? (Y or N) ")).lower() == "y":
    file_to_output = open('results.csv','w', newline='')
    csv_writer = csv.writer(file_to_output, delimiter=',')
    csv_writer.writerow(['Job Title','Job Location','Job url'])

    #adds all data, one record per row
    for i in range(0, len(job_titles)):
        csv_writer.writerow((job_titles[i], job_locations[i], job_urls[i]))
    print("File saved as results.csv!")
