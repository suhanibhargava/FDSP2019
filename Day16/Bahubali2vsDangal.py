# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:50:01 2019

@author: Dell
"""


"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""
import numpy as np
import pandas as pd

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')
temp = dataset.values

features = dataset.iloc[:, 0].values
labels1 = dataset.iloc[:, 1].values
labels2 = dataset.iloc[:,2].values

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor1.fit(features.reshape(9,1), labels1.reshape(9,1))

regressor2 = LinearRegression()
regressor2.fit(features.reshape(9,1), labels2.reshape(9,1))

print("Prediction for baahulabli",regressor1.predict(10))
print("Prediction for dangal",regressor2.predict(10))

if (regressor1.predict(10) >regressor2.predict(10)):
    print("Baahubali would collect more")
else:
    print("Dangal would collect more")





