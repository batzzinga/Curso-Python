#! /usr/bin/python
# -*- coding iso-8859-15
#Lanzar dados y que muestre los resultados hasta que salga 3
from random import randint
n = int(input("Ingrese la cantidad de lanzamientos: "))
x = 0
for i in range(n):
    x = randint(1,6)
    print (x)
    if x == 3:
        break