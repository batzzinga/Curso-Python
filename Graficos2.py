#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np
x=np.arange(-11,11)
y=2*x+3
plt.axhline(0,color="black")
plt.axvline(0,color="red")
plt.title("Grafica Lineal")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")
plt.plot(x,y)
plt.show()