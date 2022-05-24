# -*- coding: utf-8 -*-
"""
Created on Fri May  6 08:33:02 2022

@author: Mediville
"""

menu="""
Bienvenido al conversor de monedas
elija una opcio

1 convertir persos colombianos
2 convertir pesos argentinos
3 convertir pesos mexicanos

Elija una opcion """
opcion=int(input(menu))

def conversion (valordolar, pais):
    moneda=int(input(f'ingrese los pesos {pais}'))
    cambio=moneda/valordolar
    cambio=round(cambio,2)
    print(f'usted tiene {cambio} dolares' )

    
if opcion ==1:
    conversion(4000, 'colombianos')
elif opcion==2:
    conversion(65, 'argentinos')
elif opcion==3:
    conversion(24, 'mexicanos')
else:
    print('Elije una opcion valida')