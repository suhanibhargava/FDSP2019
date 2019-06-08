# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:52:41 2019

@author: Dell
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("iq_size.csv")

features = dataset.iloc[:,1:4].values
labels = dataset.iloc[:,0:1].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)
# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)
print(regressor.predict(np.array([90,70,150]).reshape(1,-1)))

