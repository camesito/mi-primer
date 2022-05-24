# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 07:52:48 2022

@author: Mediville
"""

def saludos(nombre):
    print(f'hola este es un mensaje de bienvenida para {nombre}')
saludos('carlos') 

def resta(a=None,b=None):
    if a==None or b==None:
        print('Debe digitar 2 numeros')
        return
    return a-b
r = resta(10)
print(f'la resta es {r}')

print('---'*20)
def convertircelcius (temp,unidad):
    if unidad=='K':
        grados=(temp+273.15)
    elif unidad=='F':
          grados=(temp*9/5 +32) 
    else: 
        print('Debe ingresas una unidad F o K')      
        return
    return grados
     
celcius=convertircelcius(31,'K')
print(f'la temperatura es igual a {celcius}')   