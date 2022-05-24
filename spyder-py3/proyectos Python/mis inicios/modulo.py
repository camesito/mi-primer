# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:36:55 2022

@author: Mediville
"""

def factorial(numero):
    numero=numero
    a=1
    print(f'{numero}! es ',end='')
    while numero>=1:
        if numero==1:
            print(f'{numero} ',end='')
        else:
                print(f'{numero} x ',end='')
                a=a*numero
    
        numero-=1
    
    print(f'= {a}')