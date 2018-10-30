import mysql.connector


class DataBaseConnector():

    """
    Method for connecting to the db. Must be used before everything else
    @:param user        the username of the person who has access to the mysql database
    @:param pasaword    the password of the person who has access to the mysql database
    @:return            an object to use other methods of this class
    """
    def connect(self, user, password):

        mydb = mysql.connector.connect(
            host="localhost",
            user=user,
            passwd=password
        )

        print(mydb)
        return mydb


    """
    Method for creating a new database. If it already exists, does nothing
    @:param mydb        object returned by using "connect" method from this class
    @:param db_name     the name of the database you wish to create
    @:return            0, if successful
    """
    def create_db(self, mydb, db_name):
        mycursor = mydb.cursor()

        sql = "CREATE DATABASE IF NOT EXISTS " + db_name
        mycursor.execute(sql)

        return 0

    """
    Method for using an existing database. needs to be used before using methods involving tables
    @:param mydb        object returned by using "connect" method from this class
    @:param db_name     the name of the database you wish to use
    @:return            0, if successful
    """
    def use_db(self, mydb, db_name):
        mycursor = mydb.cursor()

        sql = "USE " + db_name
        mycursor.execute(sql)

        return 0

    """
    Method for creating a table. Can only be used after method "use_db" has been used before
    @:param mydb        object returned by using "connect" method from this class
    @:param table_name  the name of the table you want to create
    @:param collums     a list. Each entry is a string with name of the collum and type.
                        Example of entry: "name VARCHAR(255)"
    @:return            0, if successful 
    """
    def create_table(self, mydb, table_name, collums):
        mycursor = mydb.cursor()

        sql = "DROP TABLE IF EXISTS " + table_name
        mycursor.execute(sql)

        sql = "CREATE TABLE " + table_name + " ("
        for collum in collums:
            sql = sql + collum
        sql = sql + ")"
        mycursor.execute(sql)

        return 0

    """
    Method for inserting an object into a table. Can only be used after method "use_db" has been used before
    @:param mydb        object returned by using "connect" method from this class
    @:param table_name  the name of the table you want to insert object into
    @:param object      a list. Each entry is a string with name of the collum and type.
                        Example of entry: "name VARCHAR(255)"
    @:return            0, if successful 
    """
    def insert_into_table(self, mydb, table_name, object):
        return