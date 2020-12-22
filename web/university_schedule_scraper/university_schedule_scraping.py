"""You will develop a Python program to dynamically complete certain tasks,
 such as list, find, sort, and save, in course listings from the scheduling portal.
 You will mainly use "request" and "BeautifulSoup" libraries (or similar, see exercise 12.1).
 The program will operate at a different level: Semester and Department.
 Your program will be a menu-based application. Assume that your project file is myproject.py.
 Once you run, it will show the last 5 semester
 (fall, spring, summer-only, (not wintersemester or, may mini semester))"""

import bs4
import requests
import time

BASE_URL = "http://appsprod.tamuc.edu/Schedule/Schedule.aspx"
TERM_1_URL = "http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term=202120"
TERM_2_URL = "http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term=202110"
TERM_3_URL = "http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term=202080"
TERM_4_URL = "http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term=202070"
TERM_5_URL = "http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term=202050"

home_res = requests.get(BASE_URL)
home_soup = bs4.BeautifulSoup(home_res.content, "lxml")

semesters = home_soup.find_all("option")
available_semesters = semesters[0:5]

print("The available semesters are:")
for semester in available_semesters:
    print(semester.text)

class DepartmentSelect():
    def __init__(self, department_url):
        self.url = department_url
        self.res = requests.get(self.url)
        time.sleep(2)
        self.soup = bs4.BeautifulSoup(self.res.content, "lxml")
        self.rows = self.soup.find_all("a", class_="nav")

#this is for testing
summer2 = DepartmentSelect( "http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term=202050")

#to do: siamo arrivati ad avere una lista di dipartimenti per semestre, #bisogna stamparla bene e parsare la pagina corsi per ogni dipartimento.
#attenzione anche a cosa dovranno fare sti corsi per capire come salvarli
