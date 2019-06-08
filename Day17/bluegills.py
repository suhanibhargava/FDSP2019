# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:21:29 2019

@author: Dell
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("bluegills.csv")
features = dataset.iloc[:,0:1].values
label = dataset.iloc[:,1:2].values

from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, label)



plt.scatter(features, label,color='green')


from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 2)
features_poly = poly_object.fit_transform(features)

x=[5]
x=np.array(x)
x=x.reshape(1,1)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, label)
print (lin_reg_2.predict(poly_object.transform(x)))




# Visualising the Polynomial Regression results
plt.scatter(features, label, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')


