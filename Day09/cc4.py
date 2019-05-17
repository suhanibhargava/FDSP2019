# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:04:05 2019

@author: Dell
"""

import sqlite3
import requests
from bs4 import BeautifulSoup


url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
data = requests.get(url).text
soup = BeautifulSoup(data,"lxml")
print(soup)
print(soup.prettify)
right_soup = soup.find("table",class_="table")
print(right_soup)


A=[]
B=[]
C=[]
D=[]

for rows in right_soup.findAll('tr'):
    cells = rows.findAll('td')
    if len(cells)==5:
            A.append(cells[1].text.strip())
            B.append(cells[2].text.strip())
            C.append(cells[3].text.strip())
            D.append(cells[4].text.strip())
            
            

#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')

# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'icc.db' )
c = conn.cursor()
c.execute("""DROP TABLE IF EXISTS ranking""")


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE ranking(
          Country TEXT,
          Weighted matches  INT,
          Points TEXT,
          Ratings INT
          )""")
for i in range (1,16):
    c.execute("INSERT INTO ranking VALUES ('"+A[i]+"','"+B[i]+"','"+C[i]+"','"+D[i]+"')")

c.execute("SELECT * FROM  ranking")
print(c.fetchall())
conn.commit()
conn.close()



# creating cursor
c = conn.cursor()