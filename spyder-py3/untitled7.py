# -*- coding: utf-8 -*-
"""
Created on Wed May 11 07:43:26 2022

@author: Mediville
"""

def run():
    contador=10000  
    operacion=0
    potencia=2**operacion
    
    while potencia < contador:
        
        if potencia==1024:
            break
        print(potencia)
        
        
        operacion+=1
        potencia=2**operacion
    # texto=input('ingrese un texto: ')
    # while texto != 'car':
    #     if letra==(' '):
    #        continue 
    #     print(letra)
        
      
    


if __name__ == '__main__':
    run()