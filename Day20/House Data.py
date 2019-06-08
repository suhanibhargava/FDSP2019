# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:12:25 2019

@author: Dell
"""
"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score

"""

import numpy as np
import pandas as pd

dataset = pd.read_csv("kc_house_data.csv")
dataset = dataset.fillna(dataset.mean())

features = dataset.drop(['price','id','date'],axis = 1)
labels = dataset['price']

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train,labels_test =	train_test_split(features, labels, test_size=0.3, random_state=1)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(features_train,labels_train)

labels_pred = lr.predict(features_test)

print("Linear regression score: ",lr.score(features_test,labels_test))


from sklearn.linear_model import Lasso
lm_lasso = Lasso() 
lm_lasso.fit(features_train, labels_train)
print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2))


from sklearn.linear_model import Ridge
lm_ridge =  Ridge() 
lm_ridge.fit(features_train, labels_train)
print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))


