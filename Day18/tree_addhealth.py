# -*- coding: utf-8 -*-
"""
Created on Thu May 30 00:54:13 2019

@author: Dell
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("tree_addhealth.csv")
labels = dataset.iloc[:,10:11]
mean = dataset.loc[:,'age'].mean()
dataset['age'] = dataset['age'].fillna(mean)