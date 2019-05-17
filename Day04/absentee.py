# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:03:20 2019

@author: Dell
"""

with open("absentee.txt","w+") as file:
        i=0
        while(i<25):
            inp = input("Enter name: ")
            file.write(inp+"\n")
            if not inp:
                break
        
with open("absentee.txt","rt") as file:
    file_content = file.read()
print("\nABSENTEES: ")
print (file_content)
        
        