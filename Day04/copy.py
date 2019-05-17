# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:53:11 2019

@author: Dell
"""

with open("c1file1.txt","rt") as file:
    file_contents=file.read()
file2 = input("Enter name of the file in which you want to copy contents: ")
with open(file2,"wt") as file:
    file.write(file_contents)
    
    