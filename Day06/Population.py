# -*- coding: utf-8 -*-
"""
Created on Tue May 14 00:32:07 2019

@author: Dell
"""
from collections import defaultdict
import csv 


#read file
with open("population.csv") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    csv_list = list(csv_reader)
    
 #select elemnets from file    
pop_dict = defaultdict(int)
for item in csv_list:
    key = "India, "+item[-1]
    pop_dict[key] += int(item[-2].replace(",",""))
print(pop_dict)