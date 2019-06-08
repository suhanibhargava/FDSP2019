# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:54:01 2019

@author: Dell
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#import dataset
from sklearn import datasets 
iris = datasets.load_iris()

iris_df	= pd.DataFrame (iris.data, columns= iris.feature_names )
iris_df['species type']= iris.target

features = iris_df.iloc[:,0:4].values
labels = iris_df.iloc[:,4].values

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
