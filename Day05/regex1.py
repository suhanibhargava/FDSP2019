# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:01:06 2019

@author: Dell
"""
import re
while True:
    inp = input("Enter a string")
    if not inp:
        break
    else:
        if re.match(r'^[+-]?\d*\.\d+$',inp):
            print("True")
        else:
            print("False")
            
    


