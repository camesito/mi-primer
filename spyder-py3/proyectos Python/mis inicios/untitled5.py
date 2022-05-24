# -*- coding: utf-8 -*-
"""
Created on Wed May  4 06:04:35 2022

@author: Mediville

 m=(a[i][j])*(b[j][i])
 m=m+m
 n.append(m)
 print(a[i][j],b[j][i])
 
 
    for j in range(0,3):
        m=(a[i][j])*(b[j][i])
        n+=m
        
    print(n)

"""

a=((1,2,3),(4,5,6))
b=((-1,0),(0,1),(1,1))
n=0
l=0
r=[(0,0),(0,0)]
p=0
q=0
    
for i in range(0,1):
    
    for j in range(0,3):

        m=(a[i][j])*(b[j][i])
        n+=m
        o=(a[i][j-1]*b[j-1][i+1])
        l+=o
        
    print(n)
    print(l)
    r[i]=n
    r[i+1]=l
 
for i in range(1,2):
    
    for j in range(0,3):

        m=(a[i][j])*(b[j][i-1])
        p+=m
        o=(a[i][j]*b[j][i])
        q+=o
    print(p)
    print(q)
    r[i]=p
    r[i+1]=q

        

print(r)       
               
        
        
       
        
        
        
    
    

        
       
        
        
    

    
        
