# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:19:00 2019

@author: Dell
"""
"""
Q1. (Create a program that fulfills the following specification.)

Import Crime.csv File.

    Perform dimension reduction and group the cities using k-means based on Rape, Murder and assault predictors.
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('crime_Data.csv')
features = dataset.iloc[:, [1,2,4]].values

labels = dataset.iloc[:, 0].values


from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)
#features_test = pca.transform(features_test)
explained_variance = pca.explained_variance_ratio_

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'low crime')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'high crime')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'medium crime')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('PCA-1')
plt.ylabel('PCA-2')
plt.legend()
plt.show()

