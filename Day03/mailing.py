# -*- coding: utf-8 -*-
"""
Created on Fri May 10 00:28:40 2019

@author: Dell
"""

old_list = ["janusfury@aol.com",
"ajlitt@me.com",
"dburrows@me.com",
"robles@yahoo.com",
"jshirley@gmail.com",
"saridder@live.com",
"dmiller@mac.com",
"agapow@yahoo.ca",
"hamilton@sbcglobal.net",
"madler@att.net",
"grady@gmail.com",
"iami@gmail.com",
"heroine@gmail.com",
"loxy@att.net",
"violinhi@icloud.com",
"morain@sbcglobal.net",
"rgiersig@gmail.com",
"jhardin@outlook.com",
"pappp@msn.com",
"hermanab@live.com",
"avollink@verizon.net",
"bulletin@yahoo.com",
"smallpaul@msn.com",
"wagnerch@hotmail.com",
"harryh@me.com",
"gbacon@live.com",
"jcholewa@yahoo.ca",
"thassine@sbcglobal.net",
"amky@me.com",
"mgreen@gmail.com",
"srour@icloud.com",
"heidrich@gmail.com",
"danzigism@me.com",
"sabren@mac.com",
"arebenti@sbcglobal.net",
"marcs@live.com",
"shrapnull@att.net",
"jguyer@mac.com",
"msherr@me.com",
"aaribaud@aol.com",
"mfleming@yahoo.com",
"seano@icloud.com",
"laird@icloud.com",
"manuals@live.com",
"mfburgo@live.com",
"budinger@optonline.net",
"udrucker@verizon.net",
"benits@outlook.com",
"baveja@mac.com",
"feamster@gmail.com",]            



new_list = ["violinhi@icloud.com",
"morain@sbcglobal.net",
"rgiersig@gmail.com",
"jhardin@outlook.com",
"pappp@msn.com",
"hermanab@live.com",
"avollink@verizon.net",
"bulletin@yahoo.com",
"smallpaul@msn.com",
"wagnerch@hotmail.com",
"harryh@me.com",
"gbacon@live.com",
"jcholewa@yahoo.ca",
"thassine@sbcglobal.net",
"amky@me.com",
"mgreen@gmail.com",
"srour@icloud.com",
"heidrich@gmail.com",
"danzigism@me.com",
"sabren@mac.com",
"arebenti@sbcglobal.net",
"marcs@live.com",
"shrapnull@att.net",
"jguyer@mac.com",
"msherr@me.com",
"aaribaud@aol.com",
"mfleming@yahoo.com",
"seano@icloud.com",
"laird@icloud.com",
"manuals@live.com",
"mfburgo@live.com",
"budinger@optonline.net",
"udrucker@verizon.net",
"benits@outlook.com",
"baveja@mac.com",
"feamster@gmail.com"]


for item in old_list:
    item.strip()
    
#print(l_old)
###

for item in old_list:
    item.strip()
    
##print(l_new)
#final=[]
#for item.lower() in l_old:
#        if item.lower() not in l_new:
#            final.append(item)
#print(final)
#s1=set(old_list)
#s2=set(new_list)
#s3=list(s1.difference(s2))
#print(s1)
#print(s2)
#print(s3)

final_list=[]
for item in old_list:
    if item not in new_list:
        final_list.append(item)
print(final_list)
        
        


    

