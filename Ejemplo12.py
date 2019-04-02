#! /usr/bin/python
# -*- coding iso-8859-15
from random import *
def adivina(n):
    n = randint(1, 6)
    return n
a = int(input("Adivina el numero: "))
for i in range(a):
    print adivina(i)
    if a == adivina(i):
        print ("Acertaste: ", a,i)
    else:
        print ("Fallo: ", a,i)
