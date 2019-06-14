# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:42:45 2019

@author: Dell
"""

import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("Dating_Data.csv" , encoding = 'latin-1')
dataset.isnull().values.any()

#What does a person look for in a partner? (both male and female)
datasetQ1 = dataset[['gender','attr1_2','sinc1_2','intel1_2','fun1_2','amb1_2','shar1_2']]
male_datasetQ1 = datasetQ1.loc[datasetQ1['gender'] == 1]
female_datasetQ1 = datasetQ1.loc[datasetQ1['gender'] == 0]


male_datasetQ1.plot.pie()

plt.pie(female_datasetQ1)