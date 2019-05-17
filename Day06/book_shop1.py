# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:55:40 2019

@author: Dell
"""

t = tuple()
l = list()
inp = [["34587" ,"Learning Python, Mark Lutz" , "4", "40.95"],["98762", "Programming Python, Mark Lutz" ,"5", "56.80"],["77226", "Head First Python,Paul Barry" ,"3", "32.95"],["88112" ,"Einführung in Python3, Bernd Klein",  "3", "24.99" ]]
for item in inp:
    x=int(item[0])
    y=int(item[2])
    z=float(item[3])
    total=round(y*z,2)
    if total<100:
        total+=10
    else:
        total
    l.append((x,total))
print(l)
    

    

ans = map(lambda x: x if x[1]>100 else (x[0]  ,x[1] + 10),map(lambda x:(int (x[0]), int (x[2]) * float(x[3]) ),inp))
print(list(ans))