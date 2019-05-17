# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:52:34 2019

@author: Dell
"""
from  selenium import webdriver
import urllib

url = "https://www.google.com/"

driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")
driver.get(url)
get_google = driver.find_element_by_id("hplogo").screenshot_as_png
with open("file2.png","wb") as file:
    file.write(get_google)


img = driver.find_element_by_xpath('//*[@id="hplogo"]')
src = img.get_attribute('src')

# download the image
urllib.request.urlretrieve(src, "captcha.png")