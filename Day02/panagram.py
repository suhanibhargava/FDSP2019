# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:21:06 2019

@author: Dell
"""

string = input("Enter string: ")
alpha = "abcdefghijklmnopqrstuvwxyz"
ispanagram = True
for word in alpha:
        if word not in string.lower():
            ispanagram = False
if ispanagram:
    print ("PANAGRAM")
else:
    print ("NOT PANAGRAM")
            