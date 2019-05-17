# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:18:32 2019

@author: Dell
"""
inp = input("Enter array").split(',')
arr=[]
for item in inp:
    arr.append(int(item))
#print(arr)

smal=min(arr)
larg=max(arr)
arr.remove(smal)
arr.remove(larg)
#print (arr)
sum=0
for item in arr:
    sum=sum+item
print(sum/len(arr))