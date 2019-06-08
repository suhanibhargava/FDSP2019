# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:33:07 2019

@author: Dell
"""

import pandas as pd
import numpy as np
import re

dataset = pd.read_csv("monster_com-job_sample.csv")

dataset = dataset[pd.notnull(dataset['salary'])]
dataset = dataset[pd.notnull(dataset['organization'])]
dataset = dataset[pd.notnull(dataset['sector'])]
dataset = dataset[pd.notnull(dataset['job_type'])]
dataset = dataset.drop(['date_added'],axis = 1)
dataset.isnull().any(axis=0)
list1=list(dataset['organization'])
for item in list1:
    r1=[]
    r1.append(re.findall("Chicago, IL",item ))