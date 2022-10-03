# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 19:18:27 2022

@author: Anton
"""

parej = dict()
n = 1
while True:
    avain = input(f"syötä avain {n}: ")
    if avain == 'stop':
        break
    arvo = input(f"syötä arvo {n}: ")
    if arvo == 'stop':
        break
    parej[avain] = arvo
    n+=1
print(parej)