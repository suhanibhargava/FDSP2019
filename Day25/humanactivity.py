# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:51:33 2019

@author: Dell
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data
train_data = pd.read_csv("train.csv") 
test_data = pd.read_csv("test.csv")

#training data
features_train = train_data.iloc[:,:-1].values
labels_train = train_data.iloc[:,562].values

#test data
features_test = test_data.iloc[:,:-1].values
labels_test = test_data.iloc[:,562].values

#Decision Tree
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test) 
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred)) 
score_dt1= classifier.score(features_test,labels_test) 
print(score_dt1)


#Random Forest
from sklearn.ensemble import RandomForestClassifier
classifier1 = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier1.fit(features_train, labels_train)  
labels_pred2 = classifier1.predict(features_test)
print(classifier1.score(features_test,labels_test))

#Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier2 = LogisticRegression()
classifier2.fit(features_train, labels_train)
labels_pred = classifier2.predict(features_test)
from sklearn.metrics import confusion_matrix
print( confusion_matrix(labels_test, labels_pred))
print(classifier2.score(features_test,labels_test))

#KNNClassifier
from sklearn.neighbors import KNeighborsClassifier
classifier3 = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier3.fit(features_train, labels_train)
labels_pred3 = classifier3.predict(features_test)
from sklearn.metrics import confusion_matrix
print( confusion_matrix(labels_test, labels_pred))
print(classifier3.score(features_test,labels_test))


print("Logistic regression is the best")


###################################################################################3

#BACKWARD ELIMINATION
import statsmodels.api as sm
#This is done because statsmodels library requires it to be done for constants.
#features = np.append(arr = np.ones((30, 1)), values = features, axis = 1)
#adds a constant column to input data set.
features = sm.add_constant(features_train)

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels_train = labelencoder.fit_transform(labels_train)
labels_test = labelencoder.fit_transform(labels_test)



features_opt = features_train
regressor_OLS = sm.OLS(endog = labels_train, exog = features_opt).fit()
regressor_OLS.summary()

y=pd.DataFrame(labels_train)
X = pd.DataFrame(features_train)
cols = list(X.columns)
pmax = 1
while (len(cols)>0):
    p= []
    X_1 = X[cols]
    X_1 = sm.add_constant(X_1)
    model = sm.OLS(y,X_1).fit()
    p = pd.Series(model.pvalues.values[1:],index = cols)      
    pmax = max(p)
    feature_with_p_max = p.idxmax()
    if(pmax>0.05):
        cols.remove(feature_with_p_max)
    else:
        break
selected_features_BE = cols
print(selected_features_BE)
features_train1 = features_train[:,selected_features_BE]
labels_train1 = labels_train
features_test1 = features_test[:,selected_features_BE]
labels_test1 = labels_test


from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train1, labels_train1)
labels_pred = classifier.predict(features_test1) 

from sklearn.metrics import confusion_matrix  
cm5 =confusion_matrix(labels_test1, labels_pred)

score_dt2 = classifier.score(features_test1,labels_test1) 
print(score_dt2)

plt.bar([0,1],[score_dt1,score_dt2],align = 'center',alpha =1,color ='yellow')
plt.show()














