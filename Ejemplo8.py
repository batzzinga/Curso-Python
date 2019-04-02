#! /usr/bin/python
# -*- coding iso-8859-15
#Simular lanzamiento del dado y que muestre la cantidad de lanzamientos hasta que resulte 5 usando while
from random import randint
x = 0
while True:
    x = randint(1,6)
    print(x)
    i=x+1
    if x == 5:
        break
print("El lanzamiento en el que salio el 5 fue: ",i)