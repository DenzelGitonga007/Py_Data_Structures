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


