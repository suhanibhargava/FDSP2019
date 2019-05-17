# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:53:03 2019

@author: Dell
"""
l=[]
import re
with open("simpsons_phone_book.txt","rt") as file:
    line = file.readlines()
    for item in line:
        if re.match(r'J.* Neu',item):
                l.append(item)
print(l)