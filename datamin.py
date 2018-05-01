# Minerador esta fazendo o download de arquivos de extensao .h(teste) e somente para o primeiro 
# nivel de arquivos nos repositorios.
# TODO 
# 	Fazer download em subdiretorios
# 	Fazer download de mais de uma usuario, por enquanto de pessoas que sigam o usuario inicial


import os
import requests
import sys
import json

# Funcao que retorna uma lista com as urls de todos os repo do usuario
def get_repos(url):

	repo_urls = []

	r = requests.get(url)

	if r.status_code == 200:
		data = r.json()

		for repo in data:
			repo_urls.append(repo['url'] + '/contents')

	return repo_urls

# Funcao que faz o download dos arquivos com uma extensao
def download_files(url_list, extensao):

	for url in url_list:

		r = requests.get(url)

		if r.status_code == 200:
			data = r.json()

			for raw in data:
				if find_ext(raw['name'], extensao):
					os.system("wget --directory-prefix=dados " + raw['download_url'])
					# print raw['download_url']

# Funcao que procura a extensao e retorna para os casos que a extensao seja a correta ou nao		
def find_ext(string, ext):
	lis_string = string.split('.')
	tam = len(lis_string)

	if tam >= 2:
		if lis_string[tam-1] == ext:
			return 1
		else: 
			return 0
	else:
		return 0			

if __name__ == '__main__':

	# user = raw_input("User: ")
	
	user = "ggpsgeorge"
	# extensao de arquivo a ser buscado nos repo
	ext = "h"

	# toda url para repositorios eh igual, o que muda eh o usuario, logo 
	# o nome de um usuario eh necessario para comecar 
	url = "https://api.github.com/users/" + user + "/repos"

	download_files(get_repos(url), ext)