# Minerador esta fazendo o download de arquivos de extensao .h(teste) e somente para o primeiro 
# nivel de arquivos nos repositorios.
# TODO 
# 	Fazer download em subdiretorios
# 	Fazer download de mais de um usuario, por enquanto de pessoas que sigam o usuario inicial


import os
import requests
import sys
import json

# Funcao retorna o json da pagina
def get_json(url, token):
	resp = os.popen("curl -H 'Authorization: token " + token + "' " + url).read()
	return json.loads(resp)


# Funcao que retorna uma lista com as urls de todos os repo do usuario
def get_repo(url,token):

	repo_urls = []

	data = get_json(url,token)

	for repo in data:
		repo_urls.append(repo['url'] + '/contents')

	return repo_urls


# Funcao que faz o download dos arquivos com uma extensao especifica
def download_files(url_list, token, extensao):

	dir_urls = []

	for url in url_list:

		data = get_json(url, token)
		
		for raw in data:

			if find_ext(raw['name'], extensao):
				file = open("dados/" + raw['name'],'w+')
				file.write(os.popen("curl -H 'Authorization: token " + token + "' " 
					+ raw['download_url']).read())
				file.close()
			if raw['type'] == "dir":
				dir_urls.append(raw['url'])

	if dir_urls != []:
		download_files(dir_urls, token, extensao)


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

# Mostra o header no json da pagina os limites de requests para uso do api
def qtd_requests(url, token):
	resp = os.popen("curl -i -H 'Authorization: token " + token + "' " + url).read()
	print resp

##########################################MAIN###################################################
if __name__ == '__main__':

	user = raw_input("User: ")
	token = raw_input("Token: ")
	ext = raw_input("Extension: ")

	# usuario inicial para a mineracao
	# user = "ggpsgeorge"

	# token de acesso eh necessario para ter autorizacao para uso pleno do api
	
	# extensao de arquivo a ser buscado nos repo
	# ext = "h"

	# toda url para repositorios eh igual, o que muda eh o usuario, logo 
	# o nome de um usuario eh necessario para comecar 
	url = "https://api.github.com/users/" + user + "/repos"
 	
	download_files(get_repo(url,token), token, ext) 

	# qtd_requests("https://api.github.com/users/ggpsgeorge/repos", token)