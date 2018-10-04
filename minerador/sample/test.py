#from data_base_connector import DataBaseConnector
#import mysql.connector
#from sqlalchemy import create


#dbconnector = DataBaseConnector()
#mydb = dbconnector.connect("root", "1234")
#dbconnector.create_db(mydb, "bdd")

from sqlalchemy import create_engine
engine = create_engine('mysql://root:1234@localhost/foo', echo=True)
