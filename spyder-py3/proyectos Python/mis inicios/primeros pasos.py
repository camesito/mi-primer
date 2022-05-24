# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#nombre = input("Digite su nombre ")
#edad = int(input("Digite su edad "))
#estatura = float(input("Digite su estarura "))
#print(f"la suma es:{edad+estatura}")
#nombre ='carlos'
#n1 = 8
#n2=7
#print (f'la suma de {n1:->10} mas {n2} es {n1+n2}')
#n1=2+4
#n2=5
#n3='control'
#n4 =True
#n5=False
edad = int(input('cual es tu Edad '))
if edad>=0 and edad<16:
    print ('Todavia no puedes conducir')
elif edad>=16 and edad<=22:
    print('Puedes conducir pero con u permiso') 
elif edad>22 and edad<=70:
        print('Puedes conducir ') 
elif edad<0:
         print('error digite una edad valida ')        
else:
    print ('requiere licencia especial')
print ("-"*20)    