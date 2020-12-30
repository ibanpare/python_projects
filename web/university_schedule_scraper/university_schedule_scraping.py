"""You will develop a Python program to dynamically complete certain tasks,
 such as list, find, sort, and save, in course listings from the scheduling portal.
 You will mainly use "request" and "BeautifulSoup" libraries (or similar, see exercise 12.1).
 The program will operate at a different level: Semester and Department.
 Your program will be a menu-based application. Assume that your project file is myproject.py.
 Once you run, it will show the last 5 semester
 (fall, spring, summer-only, (not wintersemester or, may mini semester))"""

from collections import namedtuple
import bs4
import requests

BASE_URL = "http://appsprod.tamuc.edu/Schedule/Schedule.aspx"

home_res = requests.get(BASE_URL)
home_soup = bs4.BeautifulSoup(home_res.content, "lxml")
semesters = home_soup.find_all("option")
available_semesters = semesters[0:5]

SEMESTER_1 = {f"{semesters[0].text}": f"{BASE_URL}?Term=202120"}
SEMESTER_2 = {f"{semesters[0].text}": f"{BASE_URL}?Term=202110"}
SEMESTER_3 = {f"{semesters[0].text}": f"{BASE_URL}?Term=202080"}
SEMESTER_4 = {f"{semesters[0].text}": f"{BASE_URL}?Term=202070"}
SEMESTER_5 = {f"{semesters[0].text}": f"{BASE_URL}?Term=202050"}

print("The available semesters are:")
for semester in available_semesters:
    print(semester.text)

class DepartmentSelect():
    """
    Class that scrapes departments for the selected semester
    
    TO DO:
    it should know which semester it's in
    metodi vari per sortare corsi
    """
    def __init__(self, department_url):
        self.url = department_url
        self.res = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(self.res.content, "lxml")
        self.rows = self.soup.find_all("a", class_="nav")
        self.Department = namedtuple("Department", [
            "Code",
            "Name",
            "Prefixes",
            ])
        self.departments = []
        i = 0
        while i <= len(self.rows) - 2:
            self.departments.append(self.Department(self.rows[i].text,
                self.rows[i + 1].text, self.rows[i + 2].text))
            i += 3

#this is for testing
summer2 = DepartmentSelect( "http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term=202050")

print("Here are summer2, which should need a way to know its name, departments")
for key, dep in enumerate(summer2.departments): print(dep[1])

#bisogna parsare la pagina corsi per ogni dipartimento.
#attenzione anche a cosa dovranno fare sti corsi per capire come salvarli


"""
Prefix   ID  Sec Name    Instructor  Hours   Seats   Enroll.
COSC    1301    01W Intro to Compu  Lee, Kwang  3   35  10
COSC    1436    01E Intro to Comp Sci & Prog    Brown, Thomas   4   40  36
COSC    1436    01L Intro to Comp Sci & Prog    Brown, Thomas       40  36
COSC    1436    01W Intro to Comp Sci & Prog    Hu, Kaoning 4   45  43
COSC    1436    02E Intro to Comp Sci & Prog    Hu, Kaoning 4   35  32
as first 5 rows.

il prefix è il department
ci sono vari id per department
varie sezioni per id
le hour sono nel campo del name, che gioia (regex)"""
