from view_model import ViewModel
<<<<<<< HEAD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1 - Getting a repository and putting it into an object

token = ""
#path = "https://api.github.com/repos/octocat/Hello-World"
#path2 = "https://api.github.com/repos/ggpsgeorge/minerador"
path3 = "https://api.github.com/repos/Kfourit/test2"
=======
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

>>>>>>> master
viewRepository = ViewModel(token)

<<<<<<< HEAD
# 2 - create a new session

engine = create_engine('mysql://root:1234@localhost/foo', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# 3 - generate database schema
declarative_base().metadata.create_all(engine)

# 4 - persisting data
session.add(repository)

# 5 - commit and close session
session.commit()
session.close()
=======
ls_paths = []

for user in ls_users:
	ls_paths.append(pathapi + user)

ls_repos = []
for path in ls_paths:
	ls_repos.append(viewRepository.getRepositoryFromPath(path))

print(".......%d seconds......" % (time.time() - start_time))
 	
#print(json.dumps(repository.__dict__))
>>>>>>> master
