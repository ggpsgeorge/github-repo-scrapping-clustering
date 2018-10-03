from view_model import ViewModel
import os
import json
import time

#############
# IMPORTANT #
#############
token = ""
#############
# IMPORTANT #
#############

# path1 = "https://api.github.com/repos/octocat/Hello-World"
# path2 = "https://api.github.com/repos/ggpsgeorge/minerador"
# path3 = "https://api.github.com/repos/Kfourit/test2"

pathapi = "https://api.github.com/repos"


# arq = str(input("Arquivo com usuarios e repos: "))
arq = "usersReposptest.txt"
# arq = "usersReposp1_9.txt"


start_time = time.time()

f = open(arq, "r")

ls_users = f.read().splitlines()
ls_users.pop() 

f.close()

viewRepository = ViewModel(token)

ls_paths = []

for user in ls_users:
	ls_paths.append(pathapi + user)

ls_repos = []
for path in ls_paths:
	ls_repos.append(viewRepository.getRepositoryFromPath(path))

print(".......%d seconds......" % (time.time() - start_time))
 	
#print(json.dumps(repository.__dict__))
