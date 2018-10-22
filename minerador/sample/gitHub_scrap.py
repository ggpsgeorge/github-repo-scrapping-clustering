import requests
import time
from bs4 import BeautifulSoup

class GitHub():
	
	def __init__(self, url):
		self.url = url


#############
# IMPORTANT #
#############

# Variable that defines the min and max pages in the url
# to scrap (API only accepts 9 pages per minute)

inipage = int(input("Ini: "))
finpage = inipage + 9

#############
# IMPORTANT #
#############



while(finpage < 81):



	f = open("usersReposp" + str(inipage) + "_" + str(finpage-1) + ".txt", "w")

	url = "https://github.com/search?o=desc&q=BDD&s=stars&type=Repositories&p="

	for j in range(inipage, finpage):
		github = requests.get(url + str(j))
		soup = BeautifulSoup(github.text, "html.parser")

		all_results = soup.find_all("a", attrs={"class":"v-align-middle"}, href=True)
		# print(len(all_results))
		# print(all_results[0])

		for result in all_results:
			# print(result['href'])
			f.write(result['href'] + "\n")

	f.close()

	print("Ini: %d  Fin: %d\n" % (inipage, finpage))

	time.sleep(120)

	inipage = finpage
	finpage = inipage + 9



