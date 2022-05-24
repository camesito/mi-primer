# -*- coding: utf-8 -*-
"""
Created on Fri May 20 07:27:18 2022

@author: Mediville
"""
import random

def run():
    def generar_contrasena():
        lista1=['a','b','c','d','e', 'f','g', 'h','i', 'j','k', 'l','m', 'n','o', 'p','q', 'r','s', 't','u', 'v','w', 'x','y', 'z']
        lista2=['1','2', '3','4', '5','6', '7','8', '9', '0', '#', '*','/','+','%','$']
        lista3=['']
        for i in lista1:
            lista3+=i.capitalize()
        caracteres=15
        alfabeto=lista1+lista2+lista3
        palabra=[]
        for i in range(caracteres):
            caracter_random=random.choice(alfabeto)
            palabra.append(caracter_random)
        return ''.join(palabra)
            
    contrasena=generar_contrasena()
    print(contrasena)        
    
    
    
    
if __name__ == '__main__':
    run()