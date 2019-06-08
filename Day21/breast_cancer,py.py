# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:40:16 2019

@author: Dell
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("breast_cancer.csv")
dataset.isnull()
dataset = dataset.fillna(dataset.mean())

dataset['K'] = dataset['K'].replace(2,0)
dataset['K'] = dataset['K'].replace(4,1)
