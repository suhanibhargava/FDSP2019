# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:28:57 2019

@author: Dell
"""
import numpy as np
from scipy import stats
list1 = [13, 18, 13, 14, 13, 16, 14, 21, 13]
data = np.array(list1)
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)
print("Mean: ",mean)
print("Median: ",median)
print("Mode: ",mode)