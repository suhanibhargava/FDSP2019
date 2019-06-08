# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:59:47 2019

@author: Dell
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

dataset = pd.read_csv("affairs.csv")

#spliting features and labels
labels = dataset.iloc[:,8:9].values
features = dataset.iloc[:,0:8].values

#perform one hot encoding for occupation columns
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6,7])
features = onehotencoder.fit_transform(features).toarray()

#drop 2 redundant columns after one hot encoding
cols = list(range(1,features.shape[1]))
cols.remove(6)
features = features[:,cols]

#split data
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

#scaling values
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)


# Predicting the class labels
labels_pred = classifier.predict(features_test)

#checking accuracy by score method
print("accuracy by score method: ",classifier.score(features_test,labels_test))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("confusion matrix: ",cm)

#percentage of women who had ana affair
df = pd.Series(dataset["affair"]).value_counts(normalize = True)


x = np.array([2,25,3,1,4,16,4,2])
x = onehotencoder.transform(x.reshape(1,-1)).toarray()

x = x[:,cols]
probability = classifier.predict_proba(x)



