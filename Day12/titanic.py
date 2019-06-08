# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:52:10 2019

@author: Dell
"""

import pandas as pd
df = pd.read_csv("training_titanic.csv")
#(1)
survived = df[df['Survived']==1]['Survived'].count()
print(survived)


#(2)
died =  df[df['Survived']==0]['Survived'].count()
print(died)

#(3)
males = df[df['Sex']=='male']
male_df = males['Survived'].value_counts(normalize=True)
print("maleSurvived_per: ",male_df[0]*100)
print("malediedper: ",male_df[1]*100)


females = df[df['Sex']=='female']
female_df =females['Survived'].value_counts(normalize=True)
print("femaleSurvived_per: ",female_df[0]*100)
print("femalediedper: ",female_df[1]*100)


#(4)
df['child'] = df['Age'].map(lambda x: 1 if x<18 else 0)
survived = df[df['Survived']==1]
child = survived['child'].value_counts(normalize= True)
print("child survived percent",child[1]*100)
print("adult survived percent",child[0]*100)
