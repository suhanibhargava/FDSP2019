# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:45:41 2019

@author: Dell
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels = ['a','e','i','o','u']
final_list = []

for string in state_name:
    for i in range (0,len(string)+1):
        
        if string[i] not in ['a','e','i','o','u']:
            strings_without_vowel = strings_without_vowel + string.split()

#######################################
            
for state in state_name:
    strings_without_vowel  = list()
    for letter in state.lower():
        if letter in vowels:
            continue
        strings_without_vowel.append(letter)
    final_list.append("".join(strings_without_vowel))

#######################################

for state in state_name:
    strings_without_vowel  = list(state.lower())
    for letter in vowels:
        while letter in strings_without_vowel:
            strings_without_vowel.remove(letter)
    final_list.append("".join(strings_without_vowel))


print (final_list)

#for i in range(0,len(state_name)+1):
#    for j in range(0,len(state_name[i])+1):
#        for item in vowels:
#            if(state_name[i][j]==item):
#                state_name[i].replace(item,'')
#                list1=list()
#                list1.append(state_name[i])
#print (list1)
            
        
    

#for item in state_name:
#    for item1 in vowels:
#        statesplit=item.split()
#        if item1 in item.split():
#            i=0
#            while (i<len(item)):
#                
#                item.replace(item1[i],'')
#                list1 = list()
#                list1.append(item[i])
#print (list1)
#print(statesplit)




