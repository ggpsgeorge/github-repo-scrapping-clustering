import os
import sys
import json

# Mostra o header no json da pagina os limites de requests para uso do api
def qtd_requests(url, token):
	resp = os.popen("curl -i -H 'Authorization: token " + token + "' " + url).read()
	print(resp)

token = "fd3925d2ce1816c55a92f88f922c1ff954e0f163"

qtd_requests("https://api.github.com/users/ggpsgeorge/repos", token)
