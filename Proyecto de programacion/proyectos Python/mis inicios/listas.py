# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 05:15:19 2022

@author: Mediville
"""
def main():
  dic1={'leche':0.75,'carne':10.69,'huevos':2.14, 'pan':1.07} 
  dic2 = {x:y*(1.19) for (x,y) in dic1.items()}
  print(f'el precio sin iva es {dic1}') 
  print(dic2)     
            



if __name__=='__main__' :
    main()


