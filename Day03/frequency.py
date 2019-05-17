# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:04:00 2019

@author: Dell
"""

inp = input()
d= dict()

for item in inp:
    if item not in d.keys():
        d[item]=1
    else:
        d[item]+=1
for key,values in d.items():
    print(key,values)       
        
   

    
        

