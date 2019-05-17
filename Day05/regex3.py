# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:23:09 2019

@author: Dell
"""
import re
l=[]
while True:
    inp = input()
    if not inp:
        break
    l.append(inp)
    
for item in l:
    #    if re.match(r'^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$',item):
    result = re.match(r'^[456](\d{15}|\d{3}-(\d{4}-){2}\d{4})$',item)
    check = re.search(r'(\d)\1{3,}', item.replace("-",""))
    if result and not check:
        print("Valid")
    else:
        print("Invalid")