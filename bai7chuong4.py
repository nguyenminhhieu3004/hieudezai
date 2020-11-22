# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:22:40 2020

@author: Acer
"""

import numpy as np
n= int(input("nhập số phần tử của list ="))
rd=np.random.random_sample(size = n)
print("list = ",rd)
min = rd[1]
for a in rd :
     if a < min:
         min = a
print("giá trị nhỏ nhất của list = ",min)