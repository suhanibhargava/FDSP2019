# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:30:48 2019

@author: Dell
"""

file1 = open ( 'romeo.txt',"r" )
lineList = file1.readlines()
file1.close()
print (lineList)
print ("The last line is: ")
#print lineList[len(lineList)-1]
# or simply
print (lineList[-1])