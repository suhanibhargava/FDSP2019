# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:52:13 2019

@author: Dell
"""

"""Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica and Iris versicolor).



    Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data
Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.
"""

import pandas as pd
import numpy as np 

#import dataset
from sklearn import datasets 
iris = datasets.load_iris()

iris_df	= pd.DataFrame (iris.data, columns= iris.feature_names )
iris_df['species type']= iris.target

features = iris_df.iloc[:,0:4].values
labels = iris_df.iloc[:,4].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state =0) 
                                                                            
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)
explained_variance = pca.explained_variance_ratio_

from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

#checking accuracy of model
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)

