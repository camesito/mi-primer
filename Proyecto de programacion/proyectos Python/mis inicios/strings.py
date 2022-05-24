# -*- coding: utf-8 -*-
"""
reto cadenas de strings

@author: Mediville
"""

nombre = input('escriba su nombre completo ')
#nombre = 'Carlos Alberto Medina Chaverra'
nombre=nombre.strip()
print (nombre.upper())
print (nombre.lower())
print (nombre.count('C' ,0,10))
print (nombre.find('ina'))
listanombre = nombre.split()
nombre2=''.join(listanombre)
print(nombre2)
print (f'tu nombre tiene {len(nombre2)} letras')
print(f'tu primer nombre tiene {len(listanombre[0])} letras')