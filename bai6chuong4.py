# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:56:21 2020

@author: Acer
"""
import numpy as np
n= int(input("nhập số phần tử của list ="))
rd=np.random.random_sample(size = n)
print("list = ",rd)
max = 0
for a in rd :
     if a > max:
         max = a
print("giá trị lớn nhất của list = ",max)

