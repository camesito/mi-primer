# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 07:53:07 2022

@author: Mediville
"""



def convertircelcius (temp,unidad):
    if unidad=='K':
        grados=(temp+273.15)
    elif unidad=='F':
          grados=(temp*9/5 +32) 
    else: 
        print('Debe ingresas una unidad F o K')      
        return
    return grados
     
celcius=convertircelcius(31,'C')
print(f'la temperatura es igual a {celcius}')
         
    