import os
import sys
import json

# Mostra o header no json da pagina os limites de requests para uso do api
def qtd_requests(url, token):
	resp = os.popen("curl -i -H 'Authorization: token " + token + "' " + url).read()
	print(resp)

token = "f5373952a14754f9deaefaab80e730122a399287"

qtd_requests("https://api.github.com/users/ggpsgeorge/repos", token)
