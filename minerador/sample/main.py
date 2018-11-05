from view_model import ViewModel
import time

# 1 - Initialising things ===================================================

#############
# IMPORTANT #
#############
token = "439496ca541a6de5a0cf099c5745d666a1ddce31"
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

ls_paths = []
for user in ls_users:
	ls_paths.append(pathapi + user)

ls_repos = []
for path in ls_paths:
	ls_repos.append(viewRepository.getRepositoryFromPath(path))

print(".......%d seconds......" % (time.time() - start_time))

#print(json.dumps(repository.__dict__))

# 4 - saving repositories on BD ===============================================

for repository in ls_repos:
	viewRepository.saveRepositoryOnDB(repository)
