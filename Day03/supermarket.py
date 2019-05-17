# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:13:02 2019

@author: Dell
"""


from collections import OrderedDict
od=OrderedDict()
while True:
    inp = input(" > ")
    if not inp:
        break
    l=inp.split()
    
    key,value=l[:-1],int(l[-1])
    key=" ".join(key)

#    if key in od:
#        od[key] = od[key] + value
#    else:
#        od[key] = value
    
    od[key] = od.get(key,0) + value
    
print (od)
#final=dict()
#
#for key,item in od.items():
#    if key not in final:
#        final[key]=item
#    else:
#        final[key]=final[key]+item
for key,item in od.items():
     print(key,item)
        


    

