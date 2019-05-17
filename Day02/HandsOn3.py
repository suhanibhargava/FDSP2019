# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:39:01 2019

@author: Dell
"""

def days_in_month(month):
    if month in range(1,8):
        if month%2==0:
            if month==2:
                return 28
            return 30
        else:
            return 31
    elif month in range(8,13):
        if month%2==0:
            return 31
        else:
            return 30
        
inp = int(input("Enter month:"))
days_in_month(inp)