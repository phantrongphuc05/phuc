# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:54:10 2024

@author: Admin
"""

nhap = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
#nhap = nhap.split(", ")
#print(nhap)
nhap = nhap.replace("P. ", "").replace("Q. ", "").replace("Tp. ", "")
sub_string=nhap.split(", ")
for sub in sub_string:
    print(sub)