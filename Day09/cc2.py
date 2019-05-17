# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:03:12 2019

@author: Dell
"""

import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

client = pymongo.MongoClient("mongodb://suhani_bhargav:suhani%401@cluster0-shard-00-00-exw16.mongodb.net:27017,cluster0-shard-00-01-exw16.mongodb.net:27017,cluster0-shard-00-02-exw16.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")


mydb = client.database1


def add_student(name, age, roll, branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.collection1.insert_one(
            {
            "Student name" : name,
            "Student_age" : age,
            "Student_Roll_no" : roll,
            " Student_Branch" : branch
            })
    return "Employee added successfully"


def fetch_all_student():
    user = mydb.collection1.find()
    for i in user:
        print (i)




add_student('Suhani',19, 101, 'CSE')
add_student('Saharsh',20, 206,'IT')
add_student('Stuti',21,298, 'EE')
add_student('Kunal', 23,109,'ECE')
add_student('Devendra',21,167,'IT')

fetch_all_student()