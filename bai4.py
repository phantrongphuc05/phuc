# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:31:28 2024

@author: Admin
"""
a =int(input("Nhập giờ = "))
b =int(input("Nhập phút= "))
c =int(input("Nhập giây= "))
d = (a*3600)+(b*60)+c
if a>=25:
    print("Giờ không hợp lệ.")
elif a<=24:
    print("Kết quả là: ",d)

