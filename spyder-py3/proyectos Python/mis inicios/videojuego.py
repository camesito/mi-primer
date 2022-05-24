# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:02:08 2022

@author: Mediville
"""
def juego(numero,numerorandom):
    while numero!=numerorandom:
        if numero < numerorandom:
            numero=int(input('ingrese un numero Mayor: '))
        elif numero > numerorandom:
            numero=int(input('ingrese un numero Menor: '))
    if  numero==numerorandom: 
        return True
import random    

def run():
    numero=int(input('ingrese un numero del 1 al 100: '))
    
    numeroramdom=random.randrange(100)
    
    if juego(numero, numeroramdom):
        print('resultado correcto')
        
    
    
    
if __name__=='__main__':
    run()