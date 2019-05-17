# -*- coding: utf-8 -*-
"""
Created on Tue May 14 00:32:07 2019

@author: Dell
"""
import csv
data =[]
with open("population.csv") as file:
    csv_reader = csv.DictReader(file)
    next(csv_reader)
map(lambda x:(x[])    , map(lambda x: ))