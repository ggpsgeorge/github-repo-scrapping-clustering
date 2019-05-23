from view_model import ViewModel
import time
import os

# 1 - Initialising things ===================================================

#############
# IMPORTANT #
#############
token = "4b3e390cf4b477ad3fcd0995a695d31199175b9f"
#############
# IMPORTANT #
#############

viewRepository = ViewModel(token)

# 2 - opening document with repositories to search ==========================

pathapi = "https://api.github.com/repos"

# arq = str(input("Arquivo com usuarios e repos: "))
#arq = "usersReposptest.txt"
arq = "usersReposp64_72.txt"

start_time = time.time()

f = open(arq, "r")

ls_users = f.read().splitlines()
# ls_users.pop()

f.close()

# 3 - searching repositories and saving them on objects ======================

print("Starting downloading repositories from " + arq)

ls_paths = []
for user in ls_users:
    ls_paths.append(pathapi + user)

problem_paths = []
for path in ls_paths:
    try:
        print("Downloading repository from path: " + path)
        repository = viewRepository.getRepositoryFromPath(path)
        print("Saving repository " + path + " on BD")
        viewRepository.saveRepositoryOnDB(repository)
    except:
        problem_paths.append(path)
        print("There was a problem with the repository from path: " + path)

print(".......%d seconds......" % (time.time() - start_time))

print("These repositories had problems:")
#f = open(os.mkdir("errors.txt"), "a")
for path in problem_paths:
    print(path)
    #f.write(path + "\n")
#f.close()


