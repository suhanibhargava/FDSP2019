# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:36:21 2019

@author: Dell
"""
import collections
import numpy as np
x = np.random.randint(5,15,size=40)
y = collections.Counter(x)
print(x)
print(y)
