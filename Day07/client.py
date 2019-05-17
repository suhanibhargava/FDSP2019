# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:17:04 2019

@author: Dell
"""

import requests
import json


Host = "http://13.127.155.43/api_v0.1/sending"

data = {"Phone_Number":7877757144,"Name":"Kunal Vaid","College_Name":"Amity University","Branch": "CSE"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response.json

print ( post_method().text )

def get_method():
    response = requests.get("http://13.127.155.43/api_v0.1/receiving?Phone_Number=7877757144")
    return response.json

print (get_method().text)





