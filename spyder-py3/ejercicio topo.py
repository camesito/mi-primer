# -*- coding: utf-8 -*-
"""
Created on Wed May  4 07:59:07 2022

@author: Mediville
"""

menu=['carne','arroz','ensalada','jugo','sopa','pollo']
precios=[300,75,100,50,150,180]
print('Este es el menu ')
for i in range(len(menu)):
        print(f'{i+1} {menu[i]} Valor {precios[i]}')
    
    
eleccio=input('elija las elecciones ')
eleccio=list(eleccio)

x=0
for i in eleccio:
    b=precios[int(i)-1]
    x=x+b
        

    


for i in eleccio:
    print('Su pedido es ', menu[int(i)-1], precios[int(i)-1] )

print(f'su valor total es {x}')