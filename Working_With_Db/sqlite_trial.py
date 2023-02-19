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

#import libraries
import sqlite3
from sqlite3 import Error

#Create database connection
def db_connection():
    try:
        conn = sqlite3.connect('Hoapital.db')
        return conn
    except Error:
        print(Error)
        
#Create table        
def create_tables(con):
    cursorObj = con.cursor()
    
    #Query for the first table
    cursorObj.execute(''' CREATE TABLE IF NOT EXISTS hospital_details
            (Hospital_id INT PRIMARY KEY NOT NULL UNIQUE,
             Hospital_Name TEXT NOT NULL,
             Bed_count INT NOT NULL);''')
    #Query for the second tablw
    cursorObj.execute(''' CREATE TABLE IF NOT EXISTS doctors_details
            (  Doctor_id INT PRIMARY KEY NOT NULL,
              Doctor_Name TEXT NOT NULL,
              Hospital_id INT NOT NULL,
              Date_joined TEXT NOT NULL,
              Speciality TEXT NOT NULL,
              Salary REAL NOT NULL,
              Experience TEXT NOT NULL,
              Email TEXT NOT NULL,
              UNIQUE(Doctor_id, Email)
              FOREIGN KEY (Hospital_id)
                REFERENCES hospital_details (Hospital_id) );''')
    print("Tables Created.")
    con.commit()
    
con = db_connection()

create_tables(con)

#Function to show table structure
def show_table_structure(table_name, con):
    cursorObj = con.cursor()
    # Display the structure of the hospital table
    table_info = cursorObj.execute("PRAGMA table_info("+table_name+ ");")
    print(" \t Table Structure ")
    print("=====================================\n")
    for x in table_info.fetchall():
        print(x)
    print("=====================================\n")   
#con = db_connection() 
show_table_structure('hospital_details', con)
show_table_structure('doctors_details', con)