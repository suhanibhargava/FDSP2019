# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:30:58 2019

@author: Dell
"""

import numpy as np
import pandas as pd
 

#import file
dataset = pd.read_csv("Female_Stats.csv")
features = dataset.iloc[:,1:3].values
labels = dataset.iloc[:,0:1].values

#comparing 
import statsmodels.api as sm

features = sm.add_constant(features)
features_opt = features[:, [0,1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

"""avg1 = dataset['Height'].mean()

import matplotlib.pyplot as plt
fea1 = dataset.iloc[:,1:3].values
lab1 = dataset.iloc[:,0:1].values

#plt.plot(fea1, lin_reg_1.predict(features), color = 'blue')

 #plt.scatter(fea1,lab1 )
from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(fea1, lab1)

#increase momheight by 1
dataset['momheight'] = dataset['momheight']+1
fea2 = dataset.iloc[:,1:3].values
height2 = lin_reg_1.predict(fea2)
avg2 = height2.mean()
print("When Father’s Height Is Held Constant, initial height avg = ",avg1,"avg after increasing mom height by 1 =",avg2)

#constant momheight and add 1 to every dadheight
dataset['momheight'] = dataset['momheight']-1
dataset['dadheight'] = dataset['dadheight']+1
fea3 = dataset.iloc[:,1:3].values
height3 = lin_reg_1.predict(fea2)
avg3 = height3.mean()
print("When mothers’s Height Is Held Constant, initial height avg = ",avg1,"avg after increasing mom height by 1 =",avg3)
"""