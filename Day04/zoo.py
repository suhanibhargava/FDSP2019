# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:20:37 2019

@author: Dell
"""

import csv

def show():
    with open("zoo.csv","r") as file:
        line = file.readlines()
        print("".join(line))

            
    
def group():
    animal_groups = {}
    with open("zoo.csv","r") as file:
        data = csv.reader(file,delimiter = ",")
        next(data)
        for row in data:
            if row[0] in animal_groups:
                animal_groups[row[0]][0].append(int(row[1]))
                animal_groups[row[0]][1].append(int(row[2]))
            else:
                animal_groups[row[0]] = [[int(row[1])],[int(row[2])]]
    return(animal_groups)

def water_by_group():
    
    sum=0
    group_water={}
    dict2 = group()
    for animals,info in dict2.items():
        for water_need in info[1]:
            sum=sum+water_need
        group_water[animals]=sum
    return(group_water)
water_by_group()

def total_water_need():
    sum=0
    total_need={}
    dict3=water_by_group()
    for need in dict3.values():
        sum=sum+need
    print("TOTAL NEED: ",sum)   

show()
water_by_group()
total_water_need()
 
 
        
        
        
    
    
