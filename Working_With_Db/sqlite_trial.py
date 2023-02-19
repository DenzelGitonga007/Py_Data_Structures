# Using sqlite with python
import sqlite3


#Create or connect to the database
sqlite_conn = sqlite3.connect('MyHospital.db')

print ("Database connected") # confirm that the previous line, which creates the DB, is actually ran