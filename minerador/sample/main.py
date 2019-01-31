from view_model import ViewModel
import time

# 1 - Initialising things ===================================================

#############
# IMPORTANT #
#############
token = ""
#############
# IMPORTANT #
#############

viewRepository = ViewModel(token)

# 2 - opening document with repositories to search ==========================

pathapi = "https://api.github.com/repos"

# arq = str(input("Arquivo com usuarios e repos: "))
arq = "usersReposptest.txt"
# arq = "usersReposp1_9.txt"

start_time = time.time()

f = open(arq, "r")

ls_users = f.read().splitlines()
ls_users.pop()

f.close()

# 3 - searching repositories and saving them on objects ======================

print("Starting downloading repositories from " + arq)

ls_paths = []
for user in ls_users:
    ls_paths.append(pathapi + user)

ls_repos = []
for path in ls_paths:
    print("Downloading repository from path: " + path)
    ls_repos.append(viewRepository.getRepositoryFromPath(path))

print(".......%d seconds......" % (time.time() - start_time))

#print(json.dumps(repository.__dict__))

# 4 - saving repositories on BD ===============================================

print("Starting saving repositories on Data Base")

for repository in ls_repos:
    viewRepository.saveRepositoryOnDB(repository)

