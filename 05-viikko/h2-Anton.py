# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 10:49:23 2022

@author: Anton
"""
def k_arvo(lukuja):
    if sum(lukuja) == 0 or len(lukuja) == 0:
        return 0
    return sum(lukuja) / len(lukuja)
def tup(lukuja):
    t1=tuple([sum(lukuja),len(lukuja),k_arvo(lukuja)])
    print(f"Lukujen:Summa on:{t1[0]} Määrä on:{t1[1]} Keskiarvo on:{t1[2]}")
    
lukuja = list()
i1=0
i2=i1+1
maara = int(input("syötä annettavien lukujen määrä: "))
while not(maara==i1):
    lukuja.append(int(input(f"syötä luku {i2}: ")))
    i1+=1
    i2+=1
tup(lukuja)