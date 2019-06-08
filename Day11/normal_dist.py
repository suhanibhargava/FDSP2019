# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:21:01 2019

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(150,20,1000)
plt.hist(data,100)
std = np.std(data)
print("Standard deviation: ",std)
print("Variance: ",np.var(data))