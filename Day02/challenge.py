# -*- coding: utf-8 -*-
"""
Created on Thu May  9 00:25:57 2019

@author: Dell
"""


def help():
    
    print ("What should we pick up at the store ?")
    print ("Enter 'DONE' to stop adding items.")
    print ("Enter 'SHOW' to show current status of list")
    print ("Enter 'HELP' to get help for commands")
def show(sample):
    i=1
    for item in sample:
        
        
            print("\n",i,' ',item)
            i=i+1
        

shopping_list=[]
help()
while True:
    item = input("Enter item: ")
    if item.lower()=='show':
        show(shopping_list)
        continue
    if item.lower()=='done':
        break
    if item.lower()=='help':
        help()
        break
    shopping_list.append(item)
show(shopping_list)


