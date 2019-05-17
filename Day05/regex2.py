# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:31:36 2019

@author: Dell
"""
import re
l = []
l1 = []

while True:
    inp = input()
    if not input():
        break
    l.append(inp)
    
for item in l:
    if re.match(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$',item):
        l1.append(item)

l1.sort()
print(l1)

#inp = input() 
#out = re.findall(r'[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}',"brian-23@hackerrank.commmm, britts_54@hackerrank.com, lara@hackerrank.com")
#print (out)