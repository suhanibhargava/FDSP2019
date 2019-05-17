# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:33:06 2019

@author: Dell
"""
inp = input("Enter no of small bricks,no of big bricks and target").split(',')
istarget = False
small=int(inp[0])
big=int(inp[1])
target=int(inp[2])
if (target <= small + big * 5) |  (target % 5 <= small) | (target/5 <= big):
  istarget = True

      
  
if istarget==True:
    print ("True")
else:
    print ("False")

    


