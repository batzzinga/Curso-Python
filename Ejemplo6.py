#! /usr/bin/python
# -*- coding iso-8859-15
n = int(input("Ingrese la cantidad de cauchos: "))
p = int(input("Ingrese precio del caucho: "))
costo = 0
if n >= 6:
    costo = n*p
    descuento = n*p*0.15
    total = costo-descuento
else:
    costo = n*p
    descuento = n*p*0.10   
    total = costo-descuento 
print ("Unidades; ",n)
print ("Precio x Unidad; ",p)
print ("Subtotal: ", costo)
print ("Descuento; ", descuento)
print ("Total a pagar:", int(total))
