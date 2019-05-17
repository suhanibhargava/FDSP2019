# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:11:09 2019

@author: Dell
"""
import requests
import json
city = input("Enter city name")
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+city
url3 = "&appid=cd1ee92e40d5671dcc317da693b02601"

url=url1+url2+url3
response=requests.get(url)
x = response.json()


print("Latitude and Longitude: " ,x["coord"])
print("Weather Condition: " ,x["weather"])


print("Wind Speed: " ,x["wind"]["speed"])
print("Sunset Rise and Set timing" , x["sys"]["sunrise"],x["sys"]["sunset"])
"""