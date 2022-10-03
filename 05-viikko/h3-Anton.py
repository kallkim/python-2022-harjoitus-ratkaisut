# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 20:05:17 2022

@author: Anton
"""
def fuc(numbers, devider=2):
    numbers2 = []
    for i in range(len(numbers)):
        if numbers[i] % devider == 0:
            numbers2.append(numbers[i])
    print(numbers2)

fuc([2,3,4,5,6,7,8,9],3)