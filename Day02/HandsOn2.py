# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:34:37 2019

@author: Dell
"""
def leap(year):
       if year%4==0 :
           return True
       else:
           return False
   
inp = int(input("Enter year"))
leap(inp)
