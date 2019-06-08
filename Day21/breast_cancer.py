# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:40:16 2019

@author: Dell
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("breast_cancer.csv")
dataset.isnull()
#dataset = dataset.fillna(dataset.mean())

dataset['K'] = dataset['K'].replace(2,0)
dataset['K'] = dataset['K'].replace(4,1)

dataset = dataset.fillna(dataset['G'].value_counts().index[0])

features = dataset.iloc[:,1:10].values
labels = dataset.iloc[:,10].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

#checking accuracy of model
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
# Model Score
score = classifier.score(features_test,labels_test)
# Predicting the Test set results

x = [6,2,5,3,9,4,7,2,2]
x = np.array(x)
x = x.reshape(1,-1)
prediction = classifier.predict(x)