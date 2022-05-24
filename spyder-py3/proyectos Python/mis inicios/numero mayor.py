# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:44:09 2022

@author: Mediville
"""

l=[7, 75, 46, 22, 80, 8, 81,5,10,2,48,105,658,4,12,17,633,52]
r=list(l)
while len(l)!=1:
    for i in range(len(l)-1,-1,-1):
        if l[i]<l[i-1]:
            l.pop(i)
       
    
print(l)
# for i in range(len(r)-1,-1,-1):
#     if r[i]<r[i-1]:
#         r.pop(i)
# for i in range(len(r)-1,-1,-1):
#     if r[i]<r[i-1]:
#         r.pop(i)        
    
# print('el numero mayor es ', r ,'el numero menor es ', l)          
        