# -*- coding: utf-8 -*-
"""
Created on Wed May 15 12:25:45 2019

@author: Dell
"""
from collections import OrderedDict
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver


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
    
col_name = ["Bid No","Items","Quantity","Department Name and Adress","Start date","Start Time","End Date","End Time"]
col_data = OrderedDict(zip(col_name,[bid_no,items,quantity,dept,start_date,start_time,end_date,end_time]))
df = pd.DataFrame(col_data) 
df.to_csv("bid.csv")


    
print(A)
print(B)//
