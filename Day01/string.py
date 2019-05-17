# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:17:05 2019

@author: Dell
"""

inp=input()
l=len(inp)
j=inp.find(" ")
print(inp[j+1:l],inp[0:j])
