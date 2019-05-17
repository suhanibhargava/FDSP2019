# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:39:01 2019

@author: Dell
"""

print("Enter assignments marks")
A1 = int(input())
A2 = int(input())
A3 = int(input())
print("Enter exams marks")
E1 = int(input())
E2 = int(input())
wscore = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
print(wscore)


