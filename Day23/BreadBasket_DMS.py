# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:24:35 2019

@author: Dell
"""
"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
"""

import pandas as pd
import numpy as np
from apyori import apriori
import matplotlib.pyplot as plt

# pie chart
dataset = pd.read_csv('BreadBasket_DMS.csv')
top_selling = dataset['Item'].value_counts()
top = top_selling.head(15)
plt.pie(list(top), labels=list(top.index), startangle=90, autopct='%.1f%%')
plt.show()


################################################################################################
#df = dataset.groupby('Transaction')

    
transactions =[]

def convert_to_list(arg):
    transactions.append(list(arg))
    
dataset.groupby(['Transaction'])['Item'].apply(convert_to_list)


rules = apriori(transactions, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

# Visualising the results
results = list(rules)


for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")









