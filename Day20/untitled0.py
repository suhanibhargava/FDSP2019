# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:51:53 2019

@author: Dell
"""
"""
Code Challenge 01: (Prostate Dataset)

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.
(a) Train the unregularized model (linear regressor) and calculate the mean squared error.
(b) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error."""

import numpy as np
import pandas as pd
dataset = pd.read_csv("Prostate_Cancer.csv")
dataset = dataset.replace(np.nan,0.0)

#split into features and and labels
labels = dataset["diagnosis_result"]
features = dataset.iloc[:,2:10].values

#split data
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)

#standard scaling on features
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

