# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:51:53 2019

@author: Dell
"""
"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""
import numpy as np
import pandas as pd
dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delim_whitespace = True)
dataset = dataset.replace(np.nan,0.0)

#split into features and and labels
features = dataset.iloc[:,0:8].values
labels = dataset.iloc[:,8].values

#split data
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)

#standard scaling on features
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

#apply linear regression 
from sklearn.linear_model import LinearRegression 
lr = LinearRegression ()
lr.fit(features_train, labels_train)
labels_pred = lr.predict(features_test)

#calculate mean squared error
from sklearn import metrics
print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, labels_pred),2) )


from sklearn.linear_model import Ridge
lm_ridge =  Ridge() 
lm_ridge.fit(features_train, labels_train)
predict_test_ridge = lm_ridge.predict(features_test)
print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))


from sklearn.linear_model import Lasso
lm_lasso = Lasso()
lm_lasso.fit(features_train, labels_train)
predict_test_lasso = lm_lasso.predict (features_test) 
print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

#############################################################################################

mean = labels.mean()
print(mean)
dataset['lpsa']= dataset['lpsa'].apply(lambda x: 'high' if x > mean else 'low' ,[dataset['lpsa']] )



