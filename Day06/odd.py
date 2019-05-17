# -*- coding: utf-8 -*-
"""
Created on Tue May 14 00:18:18 2019

@author: Dell
"""
from functools import reduce
l=[]
i=1
while(i<5):
    inp = input()
    if not inp:
        break
    l.append(inp)
    
def is_odd(x):
    if int(x)%2 == 1:
        return True
    
def mul(x,y):
    return int(x)*int(y)
    
def productOfOdds(l):
    return reduce(mul, filter(is_odd, map(lambda x:int(x), l)))

productOfOdds(l)