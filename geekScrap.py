
from bs4 import BeautifulSoup
import requests

def navigate(choice):
	if choice == "y":
		full_story(url_full_article)
	elif choice == "q":
		exit()
	else:
		pass

def full_story(url_full_article):
	html = requests.get(url_full_article)
	soup = BeautifulSoup(html.content,"html.parser")

	content = soup.find_all('p')
	preserved = soup.find_all('pre')
	for i in range(len(content)-6):
		print content[i].getText().encode("utf-8")
	print "-"*100
	 
	for i in range(len(preserved)):
		print preserved[i].getText().encode("utf-8")
	raw_input()




html = requests.get("http://www.geeksforgeeks.org/")
soup = BeautifulSoup(html.content.decode('utf-8','ignore'),"html.parser")

heads = soup.find_all('h2')
Text = soup.find_all('p')




for i in range(len(Text)):
	print heads[i].getText().encode("utf-8")
	print Text[i].getText().encode("utf-8")
	url_full_article = Text[i].a.get("href") 
	print ""
	print ""
	print ""
	choice = raw_input("Press y to read more and key for next article. To quit press q  : ")
	navigate(choice)
	
	print '*'*100



