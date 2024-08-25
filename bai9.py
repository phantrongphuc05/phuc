# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:27:33 2024

@author: Admin
"""
import math 
a= float(input("Nhập số a= "))
b= float(input("Nhập số b= "))
S= ((math.pow(a, 1/2)-math.pow(b, 1/2))/(math.pow(a, 1/4)-math.pow(b, 1/4)))-((math.pow(a, 1/2)+math.pow(a*b, 1/4))/(math.pow(a, 1/4)+math.pow(b,1/4)))
print("Kết quả là: ",S)