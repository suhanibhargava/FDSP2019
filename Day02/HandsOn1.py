# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:22:58 2019

@author: Dell
"""

l = list()
for item in range(1,21):
    l.append(item)
    
print ("Even :",l[1:len(l):2])
print("Odd",l[0:len(l):2])