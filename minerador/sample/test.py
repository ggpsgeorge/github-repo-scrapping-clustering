#from data_base_connector import DataBaseConnector
#import mysql.connector
#from sqlalchemy import create


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
repository1 = Repository()
repository1.setRepository("path", "name", "owner", "country", "language", [])

# 4 - persisting data
session.add(repository1)

# 5 - commit and close session
session.commit()
session.close()
