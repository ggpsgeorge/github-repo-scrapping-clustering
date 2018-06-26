# Minerador esta fazendo o download de arquivos de extensao .h(teste) e somente para o primeiro
# usario
# TODO 
# 	Fazer download de mais de um usuario, por enquanto de pessoas que sigam o usuario inicial


import os
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


# Funcao que faz o download dos arquivos em dirs e subdirs com uma extensao especifica
def download_files(url_list, token, extensao):

	dir_urls = []

	for url in url_list:

		data = get_json(url, token)
		
		for raw in data:

			if find_ext(raw['name'], extensao):
				file = open("dados/" + raw['name'],'w')
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

# Funcao pega login e id de followers da pagina
def get_followers(url,token):

	ls_follower = []

	data = get_json(url,token)

	for raw in data:
		ls_follower.append((raw['id'],raw['login']))
	
	return ls_follower

# Funcao pega todos os followers de ate x paginas(pages) de um usuario
def all_followers(url, token, pages):
	ls_followers = []

	if pages < 2:
		ls_followers = get_followers(url, token) + ls_followers
	else:
		for i in xrange(1,pages):
			ls_followers = get_followers(url + "?page=%d" % i, token) + ls_followers

	return ls_followers

			



##########################################MAIN###################################################
if __name__ == '__main__':

	# para uso manual no terminal descomente
	# user = raw_input("User: ")
	# token = raw_input("Token: ")
	# ext = raw_input("Extension: ")

	# usuario inicial para a mineracao
	# user = "ggpsgeorge"
	# user = "torvalds"
	user = "aslakhellesoy"

	# token de acesso eh necessario para ter autorizacao para uso pleno da api
	token = "47fccc67711f9f8a59348708ae3edf328750b661"

	# extensao de arquivo a ser buscado nos repo
	ext = "feature"

	# toda url para repositorios eh igual, o que muda eh o usuario, logo 
	# o nome de um usuario eh necessario para comecar 
	url = "https://api.github.com/users/" + user + "/repos"

	# precisa da url de followers e uma quantidade maxima de paginas para buscar em cada
	# usuarios
	followers_url = "https://api.github.com/users/" + user + "/followers"
	qtd_pages = 3

	# download_files(get_repo(url,token), token, ext) 
	ls_users = all_followers(followers_url, token, qtd_pages)

	# ls_users.sort()
	# print ls_users

	file = open("sortedlogins.txt","w")
	for i in ls_users:
		file.write(str(i) + "\n")

	line_count = 0

	while(line_count < 100):

		for user in ls_users:
			url = "https://api.github.com/users/" + user[1] + "/repos"
			download_files(get_repo(url,token), token, ext)
		
		followers_url = "https://api.github.com/users/" + file.readline(line_count)[1] + "/followers"	
		ls_users = all_followers(followers_url, token, qtd_pages)

		for i in ls_users:
			file.write(str(i) + "\n")

		line_count += 1
	file.close()

	# qtd_requests("https://api.github.com/users/ggpsgeorge/repos", token)