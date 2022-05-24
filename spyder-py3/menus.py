# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 07:11:33 2022
menus dentro de python con condicionales

@author: Mediville
"""
menu =""" Elija una de las siguienets opciones
    opcion 1 su nombre
    opcion 2 su edad
    opcion 3 su correo
    """
print(menu) 

opcion = input('elija una opcion entre 1 2 o 3 ')
if opcion == '1':
    nombre= input('Cual es su nombre ')
    if nombre.isalpha():
        print(f'Tu nombre es {nombre}')
    else: print('ingreso un valor no valido')
elif opcion == '2':
    edad= input('Cual es su edad ') 
    if edad.isnumeric():
        print(f'Tu nombre es {edad}')
    else: print('ingreso un valor no valido')
elif opcion == '3':
    correo= input('Cual es su correo ') 
    if correo.find('@')>=0 and correo.find('.')>=0:
        print(f'Tu correo es {correo}')
    else: print('ingreso un correo invalido')
else: print ('digite una opcion entre 1 y 3' ) 
print ('-'*20)     