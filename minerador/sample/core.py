# Minerador esta fazendo o download de arquivos de extensao .feature de usuarios que seguem o 
# usuario inicial
# TODO 
 	# Melhorar desempenho pelo pipe, desenvolver formas de manter logs para continuar mineracao
 	# apos parada
 	# Refatorar codigo para melhor manutencao e compatibilidade com orientacao a objetos


import os
import sys
import json

#deprecated

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



# Funcao pega login e id de followers da pagina
def get_followers(url,token):

	ls_follower = []

	data = get_json(url,token)

	for raw in data:
		ls_follower.append((raw['id'], raw['login'], 0))
	
	return ls_follower

# Funcao pega todos os followers de ate x paginas(pages) de um usuario
def all_followers(url, token, ini_page, last_page):
	ls_followers = []

	if ini_page < 2:
		for i in xrange(1, last_page):
			ls_followers = get_followers(url + "?page=%d" % i, token) + ls_followers

	else:
		for i in xrange(ini_page, last_page):
			ls_followers = get_followers(url + "?page=%d" % i, token) + ls_followers

	return ls_followers

			
def see_commits(url,token):
	


##########################################MAIN###################################################
if __name__ == '__main__':

	# para uso manual no terminal descomente
	# user = input("User: ")
	# token = input("Token: ")
	# ext = input("Extension: ")
	
	# certos usuarios possuem uma qtd grande de followers, caso queira restringir a qtd, use
	# a proxima linha
	# ini_page, last_page = int(input("First page: ")), int(input("Last page: "))

	# usuario inicial para a mineracao
	# user = "ggpsgeorge"
	# user = "torvalds"
	# user = "aslakhellesoy"
	# user = "BorisOsipov"

	# token de acesso eh necessario para ter autorizacao para uso pleno da api
	token = "29697e714959214a9f1681a0aedb94167047b0eb"

	# extensao de arquivo a ser buscado nos repo
	# ext = "feature"

	# toda url para repositorios eh igual, o que muda eh o usuario, logo 
	# o nome de um usuario eh necessario para comecar 
	# url = "https://api.github.com/users/" + user + "/repos"

	# precisa da url de followers e uma quantidade maxima de paginas para buscar em cada
	# usuario
	# followers_url = "https://api.github.com/users/" + user + "/followers"
	
	# ini_page = 1
	# last_page = 3

	# download_files(get_repo(url,token), token, ext) 
	# ls_users = all_followers(followers_url, token, ini_page, last_page)

	# ls_users.sort()
	# print ls_users

	# file = open("logins.txt","w")
	# for i in ls_users:
	# 	file.write(str(i) + "\n")

	# while(1):

	# 	for user in ls_users:
	# 		url = "https://api.github.com/users/" + user[1] + "/repos"
	# 		download_files(get_repo(url,token), token, ext)
		
	# 	followers_url = "https://api.github.com/users/" + file.readline(line_count)[1] + "/followers"	
	# 	ls_users = all_followers(followers_url, token, qtd_pages)

	# 	for i in ls_users:
	# 		file.write(str(i) + "\n")

	# file.close()
