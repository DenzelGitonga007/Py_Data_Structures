# Using sqlite with python
import sqlite3


#Create or connect to the database
sqlite_conn = sqlite3.connect('MyHospital.db')

print ("Database connected") # confirm that the previous line, which creates the DB, is actually ran

# To execute SQLite statements in Python, you need a cursor object
#Create a cursor object
conn = sqlite_conn.cursor()

# Print sqlite version
dbversion = conn.execute("select sqlite_version();")
print("\nSQLite Database Version is: ", dbversion.fetchall())


# To create an in-memory database (stored in RAM), you can use the following code
import sqlite3
from sqlite3 import Error

def create_db():
    try:
        conn = sqlite3.connect(':memory:')
        print("Connection is established: Database is created in memory")
    except Error:
        print(Error)
    finally:
        conn.close()
    
create_db()