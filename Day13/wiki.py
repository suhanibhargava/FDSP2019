# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:44:42 2019

@author: Dell
"""
"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""
from selenium import webdriver
import matplotlib.pyplot as plt

#scrap data from url
url = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")
driver.get(url)


#append data in individual lists
states = []
nationalshare=[]
for i in range(1,7):
    get_state = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[2]/a')
    states.append(get_state.text)
    get_nationalshare =driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[5]')
    nationalshare.append(get_nationalshare.text)
nationalshare = list(map(float,nationalshare))

#draw pie chart using lists's data    
plt.pie(nationalshare,(0.1,0,0,0,0,0),states)
plt.axis('equal')
plt.show()



