# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:20:55 2019

@author: Dell
"""
import numpy as np
inp = input()
inp = list(map(int,inp.split()))
x= np.array(inp)
x=x.reshape(3,3)
print(x)