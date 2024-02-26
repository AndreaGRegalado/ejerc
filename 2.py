# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:38:22 2024
Ejercicio Numpy and Matplotlib
@author: andrea.garcia
"""
###1 Creating and Manipulating Arrays
import numpy as np
from matplotlib import pyplot as plt

#1.1. Create two 2D arrays representing coordinates x, y on the cartesian plan
##Both should cover the range (-2, 2) and have 100 points in each direction
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
x_1, y_1 = np.meshgrid(x, y)

##1.2. Visualize each 2D array using pcolormesh
plt.pcolormesh(x_1)
plt.pcolormesh(y_1)


