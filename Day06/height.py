# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:21:55 2019

@author: Dell
"""
from functools import reduce
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
          
heights = list(map(lambda x : x['height'],list(filter(lambda x : 'height' in x ,people))))


def f(x,y):
    return x+y

res = reduce(f,list(heights))
avg=res/len(heights)
print(avg)