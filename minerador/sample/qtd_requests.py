import os
import sys
import json
import requests

# Mostra o header no json da pagina os limites de requests para uso do api
# def qtd_requests(url, token):
# 	resp = os.popen("curl -i -H 'Authorization: token " + token + "' " + url).read()
# 	print(resp)

def qtd_requests(url, token):
	resp = requests.get(url, headers={'Authorization': 'token {}'.format(token)})
	print(resp.headers)

token = ""

qtd_requests("https://api.github.com/users/ggpsgeorge/repos", token)
