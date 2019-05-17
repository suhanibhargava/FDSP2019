# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:27:47 2019

@author: Dell
"""

inp = input("Enter string: ")
final_string=''
vowel='aeiou'
for c in inp:
    if c.lower()  not in vowel:
        final_string = final_string+ c+'o'+c
    else:
        final_string=final_string+c
        
        

print (final_string)