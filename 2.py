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

##1.3 From your cartesian coordinates, create polar coordinates "r" and "phi"
##You will need to use numpy’s arctan2 function. Read its documentation.

def cart2pol (x,y):
    r = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y,x)
    return r, phi

r, phi = cart2pol(x, y)

##1.4. Visualize "r" and "phi" on the 2D x/y plane using pcolormesh

##1.5 Caclulate the quanity (fórmula)

##1.6 Plot the mean of f with respect to the x axis as a function of y

##1.7 Plot the mean of f with respect to the y axis as a function of x

##1.8 1.8 Plot the mean of f with respect to   as a function of  

###2. Analyze ARGO Data

import pooch
url = "https://www.ldeo.columbia.edu/~rpa/float_data_4901412.zip"
files = pooch.retrieve(url, processor=pooch.Unzip(), known_hash="2a703c720302c682f1662181d329c9f22f9f10e1539dc2d6082160a469165009")
files