# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:39:39 2019

@author: Dell
"""

"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Automobile.csv")

new_df = df['make'].value_counts()
top = new_df.head(10)

plt.pie(top.values,(0.1,0,0,0,0,0,0,0,0,0),top.index)
plt.show()