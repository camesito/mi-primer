# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 07:53:12 2022

@author: Mediville
"""
print('opcion 1 pizza Vegetariana')
print('opcion 2 pizza no Vegetariana')
r=()
p=int(input('elija la opcio 1 o opcio 2'))
ingredientes=('Pimiento ','tofu ', 'peperoni ', 'jamon ', 'salmon ',  )
if p==1:
    print(f'pizza vegetariana dispone de los siguientes: {ingredientes[:1]}')
    r=input('elija un ingrediente ')
    print(f'su pizza es  vegetariana con los ingredientes mozzarela tomate y {r}')
else:
    print(f'pizza no vegetariana dispone de los siguientes: {ingredientes}')
    r=input('elija un ingrediente ')
    if r=='tofu' or r=='Pimiento':
        print(f'su pizza es vegetariana con los ingredientes mozzarela tomate y {r}')
    else:
        print(f'su pizza es no vegetariana con los ingredientes mozzarela tomate y {r}')
    
    