# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:58:13 2019

@author: Dell
"""


def Add(inp1):
    sum=0
    for item in inp1:
        sum=sum+item
    return sum
    
def Multiply(inp1):
    mul=1
    for item in inp1:
        mul=mul*item
    return mul
    
def Largest(inp1):
    lar=inp1[0]
    for item in inp1:
        if item>lar:
            lar=item
    return lar

def Smallest(inp1):
    smal=inp1[0]
    for item in inp1:
        if item < smal:
            smal=inp1[0]
    return smal

def Sorting(inp1):
    inp2=[]
    for item in inp1:
        inp2.append(item)      
    inp2.sort()
    return inp2

def RemoveDuplicates(inp1):
    final = []
    for item in inp1:
            if item not in final:
                final.append(item)
        
    return final

def Print():
    print("Sum =",Add(inp1))
    print("Multiply",Multiply(inp1))
    print("Largest =",Largest(inp1))
    print("Smallest = ",Smallest(inp1))
    print("Sorted list = ", Sorting(inp1))
    print("list without duplicates",RemoveDuplicates(inp1))
    
inp = (input("Enter list")).split()
inp1=[]
for item in inp:
    inp1.append(int(item))

Print()

    
        
        