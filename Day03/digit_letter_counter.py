# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:31:52 2019

@author: Dell
"""



s = input("Enter string: ")
numbers = sum(c.isdigit() for c in s)
words   = sum(c.isalpha() for c in s)
print(numbers,words)
    
    ###############################################
    
    
    
dcount=0
lcount=0
d = dict()
s = input("enter string")
for c in s:
    if c.isalpha():
        lcount=lcount+1
    if c.isdigit():
        dcount=dcount+1
d["letters"]=lcount
d["digits"]=dcount
for k,v in d.items():
    print(k,v)
        