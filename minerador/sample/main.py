from view_model import ViewModel
import os
import json


token = ""
# path1 = "https://api.github.com/repos/octocat/Hello-World"
# path2 = "https://api.github.com/repos/ggpsgeorge/minerador"
# path3 = "https://api.github.com/repos/Kfourit/test2"

pathapi = "https://api.github.com/repos/"

file = open("usersRepos.txt","r")
ls_users = file.readlines() 

viewRepository = ViewModel(token)

ls_paths = []
for user in ls_users:
	ls_paths.append(pathapi + user)

ls_repos = []
for path in ls_paths:
	ls_repos.append(viewRepository.getRepositoryFromPath(path))

for x in ls_repos:
	print(x)
 	
#print(json.dumps(repository.__dict__))
