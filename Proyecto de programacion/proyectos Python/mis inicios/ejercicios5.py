# -*- coding: utf-8 -*-
"""
Created on Sun May  1 17:20:15 2022
c=int(input('ingrese la tabla de multiplicar que desea conocer'))
p=10

for i in range(1,p):
    
    print(f'{c} x {i}= ',i*c)
    
    
    
for i in range(1,p+1):
    if i%2==1:
        for j in range(i+1):
            if j%2==1:
                print(j , end=(''))
                i-=1
        else:
         print('')    

@author: Mediville
"""
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    print(i)
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")
  

        
        
        
    
    