# -*- coding: utf-8 -*-
"""
Created on Wed May 11 15:22:38 2022

@author: Mediville
"""
def numeroesprimo(valor):
    contador=0
    for i in range(2,valor):
        if valor%i == 0:
            contador+=1
    if contador==0:
        return True
    else: 
        return False        
        
def numerosprimos2(valor):
    contador=2,3,5,7,11,13,17,19,23,29
    
    for i in contador:
        if i ==valor:
            continue
        c=valor//i
        
        
        print(c, ' ', i)
        if i>=c:
            return True
        if valor%i==0:
            return False
        
    
    
    
    
def run():
    numero=int(input('ingrese un numero: '))
    if numerosprimos2(numero):
        print('es un numero primo ')
    else:
        print('no es un numero primo')
           
   
           
           
        
            


if __name__ == '__main__':
    run()