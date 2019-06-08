# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:04:20 2019

@author: Dell
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("mushrooms.csv")


features = dataset.iloc[:,[5,20,21]].values
labels = dataset.iloc[:,0].values
labels = labels.reshape(-1,1)

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,0] = labelencoder.fit_transform(features[:, 0])
features[:,1] = labelencoder.fit_transform(features[:, 1])
features[:,2] = labelencoder.fit_transform(features[:, 2])
labels[:,0]   = labelencoder.fit_transform(labels [:, 0])
features = features.astype(float)
labels = labels.astype(float)

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0,1,2])
features = onehotencoder.fit_transform(features).toarray()





# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
