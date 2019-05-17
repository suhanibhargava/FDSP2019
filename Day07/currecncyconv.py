# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:09:52 2019

@author: Dell
"""
import json
import requests
url1="http://api.fixer.io/latest?base=USD&symbol=INR"
url2="? access_key=f130bf6178c7ac674b6d1b29731fde11"
url=url1+url2
  
response= requests.get(url)
x=response.json()

