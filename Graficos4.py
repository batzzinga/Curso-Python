#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np
x=np.array([3,1,5,7])
y=np.array([22,23,1,4])
#segundo conjunto de datos
x2=np.array([23,12,3,1])
y2=np.array([1,3,5,5])
plt.bar(x,y,align="center")
plt.bar(x2,y2,color="g",align="center")
plt.title("Grafico de Barras")
plt.show()
