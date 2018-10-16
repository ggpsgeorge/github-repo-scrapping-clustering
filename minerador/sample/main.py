from view_model import ViewModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1 - Getting a repository and putting it into an object

token = ""
#path = "https://api.github.com/repos/octocat/Hello-World"
#path2 = "https://api.github.com/repos/ggpsgeorge/minerador"
path3 = "https://api.github.com/repos/Kfourit/test2"
viewRepository = ViewModel(token)
repository = viewRepository.getRepositoryFromPath(path3)
#print(repository)

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