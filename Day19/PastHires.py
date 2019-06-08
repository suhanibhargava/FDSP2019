# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:46:13 2019

@author: Dell
"""
"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.
"""


import pandas as pd
import numpy as np

dataset = pd.read_csv("PastHires.csv")

features = dataset.iloc[:,0:6].values
labels = dataset.iloc[:,6:7].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,1] = labelencoder.fit_transform(features[:, 1])
features[:,3] = labelencoder.fit_transform(features[:, 3])
features[:,4] = labelencoder.fit_transform(features[:, 4])
features[:,5] = labelencoder.fit_transform(features[:, 5])
labels[:,0]   = labelencoder.fit_transform(labels [:, 0])
features = features.astype(float)
labels = labels.astype(float)

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)

from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred)) 


from sklearn.ensemble import RandomForestClassifier

classifier1 = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier1.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

x = [10,1,4,0,1,0]
x = np.array(x)
x = x.reshape(1,-1)
print(classifier1.predict(x))
y =[10,0,4,1,0,1]
y = np.array(y)
y = y.reshape(1,-1)
print(classifier1.predict(y))



