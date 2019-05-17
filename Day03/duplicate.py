# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:32:01 2019

@author: Dell
"""

l = [12,24,35,24,88,120,155,88,120,155]
s = set()
for item in l:
    if item not in s:
        s.add(item)
s=list(s)
print(s)
 