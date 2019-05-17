# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:12:56 2019

@author: Dell
"""

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

codes = map(lambda x : random.choice(code_names),names)
print(list(codes))

