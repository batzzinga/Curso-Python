#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np
datos = [[1, 2, 3, 4], [3, 5, 3, 5], [18, 6, 4, 2]]
X = np.arange(4)
plt.bar(X + 0.00, datos[0], color = "b", width = 0.25)
plt.bar(X + 0.25, datos[1], color = "g", width = 0.25)
plt.bar(X + 0.50, datos[2], color = "r", width = 0.25)
plt.xticks(X+0.38, ["A","B","C","D"])
plt.show()ls