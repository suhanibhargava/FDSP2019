# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:06:54 2019

@author: Dell
"""
list1=[]
with open("romeo.txt") as file:
#    for line in file:
        line = file.read().split()
        for i in line:
            if i[-1]=="\n":
                i=i[:-1]
            list1.append(i.split(" "))
word_count={}
for word in line:
    if word not in word_count:
        word_count[word]=1
    else:
        word_count[word]+=1
for k,v in word_count.items():
    print(k,v)