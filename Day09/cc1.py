# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:03:11 2019

@author: Dell
"""

import sqlite3
from pandas import DataFrame

#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')

# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'student.db' )


# creating cursor
c = conn.cursor()
c.execute("""DROP TABLE IF EXISTS Student""")


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE Student(
          name STRING,
          age  INT,
          ROLL INT,
          branch String
          )""")


# STEP 2
c.execute("INSERT INTO Student VALUES ('Suhani',19,145, 'CSE')")
c.execute("INSERT INTO Student VALUES ('Yogendra',18,167 ,'IT')")
c.execute("INSERT INTO Student VALUES ('Pradeep',20,101, 'ECE')")
c.execute("INSERT INTO  Student VALUES ('Kunal',20,198, 'EE')")
c.execute("INSERT INTO  Student VALUES ('Devendra',20,167, 'EEE')")


# STEP 3
c.execute("SELECT * FROM Student")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
#print ( c.fetchone()) 

# returns one or otherwise None as a tuple
#print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall())


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM Student")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()
