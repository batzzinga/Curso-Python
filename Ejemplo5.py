#! /usr/bin/python
# -*- coding iso-8859-15
from random import *
n = int(input("Ingrese la cantidad de intentos: "))
gana = 0
for i in range(n):
    x = randint(1,6)
    if x == 6:
        gana = gana + 600
    elif x == 3:
        gana = gana + 300
    elif x == 1:
        print("Debe seguir jugando")
    else:
        gana = gana - 50
if gana >=0:
    print ("La ganancia es: ", gana)
else:
    print ("La perdida es: ", gana)