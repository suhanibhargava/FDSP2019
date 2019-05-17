# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:06:11 2019

@author: Dell
"""
sample = input("Enter numbers: ").split()
all_pos = True
palindrome = False

for i in sample:
    if int(i) < 0:
        all_pos = False

if all_pos:
    for i in sample:
        if i == i[::-1]:
            palindrome = True

if palindrome:
    print("palindrome")
else:
    print("Not Palindrome")
    
#####################################################

 for item in l:
     if int(item)>0 :
         if item[::-1]== item:
             
        
         
             
         
             print("True")
         else:
             print("False")
     else:
         print("False")
                
    


     
 
 
 
# for item in l:
#     
#     l1.append(int(item))
#     for item1 in l1:
#         if item1>0 & str(item1)[::-1]==str(item1):
#             print("True")
#         else: 
#             print("False")
#     

     


