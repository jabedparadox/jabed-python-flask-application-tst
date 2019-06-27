# instance/config.py

SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'mysql://jabed_admin:239416@localhost/jabedproject_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

#import pyodbc
#import MySQLdb
#database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "test")
#cursor = database.cursor()

# INSERT INTO test table
#query = """
#INSERT INTO test (
#    name,
#    age
#) VALUES (?, ?)"""

#values = (name,age)

# create table
#cursor.execute(query, values)
#database.commit()

# close database connection
#database.close()
