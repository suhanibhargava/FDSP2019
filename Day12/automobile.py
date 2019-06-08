# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:02:50 2019

@author: Dell
"""

import pandas as pd
import numpy as np
df = pd.read_csv("Automobile.csv")
new_df= df.fillna(0)

prices = np.array(new_df['price'])

print("min",prices.min())
print("max",prices.max())
print("std",prices.std())