#dbconnector = DataBaseConnector()
#mydb = dbconnector.connect("root", "1234")
#dbconnector.create_db(mydb, "bdd")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Repository, Feature

# 1 - create a new session

engine = create_engine('mysql://root:1234@localhost/foo', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# 2 - generate database schema
declarative_base().metadata.create_all(engine)

# 3 - create repository
feature1 = Feature()
feature1.path = "path1"
feature1.name = "name1"
features = []
features.append(feature1)
repository1 = Repository()
repository1.setRepository("path", "name", "owner", "country", "language", 1, features)


# 4 - persisting data
session.add(repository1)

# 5 - commit and close session
session.commit()
session.close()

