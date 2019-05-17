# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:15:21 2019

@author: Dell
"""

days = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
inp = input("Enter days: ").split(',')

#final_list=[]
#for item in days:
#    if item not in inp:
#        final_list.append(item)
#
#print(tuple(final_list+inp))


final_list=[]
i=0
while(i<8):
    for item in days:
        if item not in inp:
            final_list.append(days[i])
        else:
            final_list.append(inp[i])
            
print(tuple(final_list))

