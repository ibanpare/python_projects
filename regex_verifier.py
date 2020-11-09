"""
A tool that allows the user to enter a text string and then 
in a separate control enter a regex pattern. 
It will run the regular expression against the source text 
and return any matches or flag errors in the regular expression.
An example is https://www.regextester.com/
"""

import re

def regexverify(pattern = "", string = ""):
	pattern = input("Please insert your pattern: ")
	string = input("Please enter your string: ")
	if re.findall(pattern, string):
		print("Perfect, your pattern matches!")
	else:
		print("Sorry, no match!")

if __name__ == '__main__':
	regexverify()