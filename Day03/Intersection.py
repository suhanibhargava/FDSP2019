# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:42:18 2019

@author: Dell
"""

l1=[1,3,6,78,35,55] 
l2= [12,24,35,24,88,120,155]
s1=set(l1)
s2=set(l2)
s3=s1.intersection(s2)
print(list(s3))