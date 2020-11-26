"""You will develop a Python program to dynamically complete certain tasks,
 such as list, find, sort, and save, in course listings from the scheduling portal.
 You will mainly use "request" and "BeautifulSoup" libraries (or similar, see exercise 12.1).
 The program will operate at a different level: Semester and Department.
 Your program will be a menu-based application. Assume that your project file is myproject.py.
 Once you run, it will show the last 5 semester
 (fall, spring, summer-only, (not wintersemester or, may mini semester))"""

import mechanicalsoup

BASE_URL = "http://appsprod.tamuc.edu/Schedule/Schedule.aspx"
browser = mechanicalsoup.StatefulBrowser()
main_page = browser.get(BASE_URL)
soup = main_page.soup

#gets top five semesters
all_semesters = soup.find_all("option")
top_five_semesters = []

for n in range(0,5):
	last_semester = all_semesters[n].get_text()
	top_five_semesters.append(last_semester)

"""
User will make selection, then, you will show departments for the selected semester (Fall 2020). Note that selected semester is visible before a ">" sign.

Fall 2020> Select a department:
1) Undeclared
2) Accounting and Finance
3) Art
4) Ag Science & Natural Resources
...
...
30) Social Work
31) Theatre
Q)Go back

Selection: 3
"""

"""
qui selezioniamo il form che ci interessa in base al nome e impostiamo
il valore con il semestre che l'utente ha scelto
poi submittiamo e abbiamo la pagina che ci interessa con i corsi

poi bisognerà fare selezione del department
"""

browser.open(BASE_URL)
browser.select_form()
browser["ctl00$LefyContent$ddlterm"] = "Summer II 2020"
browser.submit_selected()
semester_page = browser.get_current_page()

departments_html = semester_page.find_all("a", class_ = "nav")
departments = []
for i in range(0, len(departments_html)):
	departments.append(departments_html[i].get_text())

print(departments)

#come sopra prende tutte le colonne, aiutooo, più data cleaning o prendiamo e mostriamo diversamente