import requests
from bs4 import BeautifulSoup

class GitHub():
	
	def __init__(self, url):
		self.url = url

file = open("usersRepos.txt","w")

# Variable that defines de max page in the url
maxpage = 3

url = "https://github.com/search?o=desc&q=BDD&s=stars&type=Repositories&p="

for j in range(1, maxpage):
	github = requests.get(url + str(j))
	soup = BeautifulSoup(github.text, "html.parser")

	all_results = soup.find_all("a", attrs={"class":"v-align-middle"})
	# print(len(all_results))
	# print(all_results[0])

	for i in range(len(all_results)):
		file.write(all_results[i].contents[0] + "\n")

file.close()