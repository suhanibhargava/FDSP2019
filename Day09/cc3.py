# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:06:13 2019

@author: Dell
"""

from collections import OrderedDict
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
import mysql.connector 
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='suhani_bhargav', password='7life7sucks7',
                              host='db4free.net', database = 'suhanidb')
#, database = 'forsk_test'

# creating cursor
c = conn.cursor()



url = "https://bidplus.gem.gov.in/bidlists"

driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")
driver.get(url)

bid_no=[]
items=[]
quantity=[]
dept=[]
start=[]
end=[]






for i in range(1,11):
    get_bid_no = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    bid_no.append(get_bid_no.text)
    get_items = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span')
    items.append(get_items.text)
    get_quantity = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/strong')
    quantity.append(get_quantity.text)
    get_department =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]')
    dept.append(get_department.text)
    get_start=  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span')
    start.append(get_start.text)
    get_end= driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span')
    end.append(get_end.text)
start_date=[]
start_time=[]
end_date=[]
end_time=[]    
for item in start:
    start_date.append(item.split()[0])
    start_time.append(item.split()[1]+item.split()[2])
    
for item in end:
    end_date.append(item.split()[0])
    end_time.append(item.split()[1] + item.split()[2])
    
c.execute("DROP Table IF EXISTS BID;")

# STEP 3
c.execute ("""CREATE TABLE BID(
          bid TEXT,
          items  TEXT,
          quantity TEXT,
          department TEXT,
          start_date TEXT,
          start_time TEXT,
          end_date TEXT,
          end_time TEXT
          )""")

for i in range(0,9):   
    c.execute("INSERT INTO BID VALUES ('"+bid_no[i]+"','"+items[i]+"','"+quantity[i]+"','"+dept[i]+"','"+start_date[i]+"','"+start_time[i]+"','"+end_date[i]+"','"+end_time[i]+"')")


c.execute("SELECT * FROM  BID")
print(c.fetchall())
conn.commit()
conn.close()
