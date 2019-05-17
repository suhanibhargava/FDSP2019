# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:39:12 2019

@author: Dell
"""
def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    else:
        return n
    
    
inp = input("Enter the dictionary: ")
from ast import literal_eval
sample = literal_eval(inp)
print(sample)
sum=0

for value in sample.values():
    val=fix_teen(value)
    sum=sum+val
    
print("sum",sum)







