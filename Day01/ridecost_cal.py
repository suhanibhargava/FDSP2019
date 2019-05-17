# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:37:17 2019

@author: Dell
"""

dist=float(input("Enter the distance in km"))
cost=int(input("Enter cost of diesel"))
avg=int(input("Enter vehicle/'s average"))
print("Total amount",float(dist/avg)*cost)