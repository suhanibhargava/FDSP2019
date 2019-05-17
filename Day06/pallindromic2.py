# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:27:13 2019

@author: Dell
"""
inp = input().split(' ')
if all(int(x)>0 for x in inp) and any(x==reversed(x) for x in inp ):
    print("True")
      
else:
    print("False")
        

    