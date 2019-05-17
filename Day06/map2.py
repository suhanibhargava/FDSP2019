# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:16:49 2019

@author: Dell
"""

names = ['Mary', 'Isla', 'Sam']




codes = map(lambda x:hash(x),names)
print(list(codes))