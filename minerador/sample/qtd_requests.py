import os
import sys
import json

token = ""

# Mostra o header no json da pagina os limites de requests para uso do api
def qtd_requests(url, token):
	resp = os.popen("curl -i -H 'Authorization: token " + token + "' " + url).read()
	print(resp)

qtd_requests("https://api.github.com/users/ggpsgeorge/repos", token)
