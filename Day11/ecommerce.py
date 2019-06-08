# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:53:14 2019

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20, 10000)
print (incomes)
plt.hist(incomes,bins=50)
plt.show()
mean = np.mean(incomes)
median = np.median(incomes)
print(mean)
print(median)