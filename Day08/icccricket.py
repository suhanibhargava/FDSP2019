# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:16:58 2019

@author: Dell
"""

import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import pandas as pd

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
            
            


col_name = ["Country","Weighted matches","Points","Ratings"]
col_data = OrderedDict(zip(col_name,[A,B,C,D]))
df = pd.DataFrame(col_data) 
df.to_csv("icc.csv")

        
    
    