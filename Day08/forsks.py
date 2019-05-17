# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:51:05 2019

@author: Dell
"""
import requests
url = "http://forsk.in/images/Forsk_logo_bw.png"
source=requests.get(url)
with open("downlaod.png","wb") as file:
    file.write(source.content)
    