# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:36:51 2019

@author: Dell
"""

"""Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)

"""
import numpy as np
import pandas as pd

dataset = pd.DataFrame()


#reading data into dataframe
dataset = pd.read_table("Auto_mpg.txt",delim_whitespace = True ,header = None,names = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"])
#car name with max mpg
car_name = dataset["car name"][dataset["mpg"] == dataset["mpg"].max()]
#max mpg value
#max_value = dataset.sort_values(by = 'mpg',ascending = 0)
#car_name = max_value.iloc[0,8]
#print("car name with highest mpg: ",car_name)

#
features = dataset.drop(['mpg','car name'],axis =1)
labels = dataset['mpg']

features['horsepower'] = features['horsepower'] .replace('?',0.0)



from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)


from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df  

regressor.score(features_test,labels_test)



from sklearn.ensemble import RandomForestRegressor

regressor1 = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor1.fit(features_train, labels_train)  
labels_pred = regressor1.predict(features_test)  

x = [6,215,100,2630,22.2,80,3]
x = np.array(x)
x = x.reshape(1,-1)

print("Decision Tree",regressor.predict(x))
print("Random Forest",regressor1.predict(x))


