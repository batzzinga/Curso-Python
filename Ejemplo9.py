#! /usr/bin/python
# -*- coding iso-8859-15
#Simular lanzamiento del dado y que muestre la cantidad de lanzamientos hasta que resulte 5 usando for
from random import randint
n = int (input("Ingrese la cantidad de lanzar el dado: "))
x = 0
for i in range(n):
    x = randint(1,6)
    print(x)
    if x == 5:
        break
print("El lanzamiento en el que salio el 5 fue: ",i+1)