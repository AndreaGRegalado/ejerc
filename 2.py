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
import numpy as np
from matplotlib import pyplot as plt
#import os
url = "https://www.ldeo.columbia.edu/~rpa/float_data_4901412.zip"
files = pooch.retrieve(url, processor=pooch.Unzip(), known_hash="2a703c720302c682f1662181d329c9f22f9f10e1539dc2d6082160a469165009")
files

##2.1 Load each data file as a numpy array.
type(files)
#Trabajar con los directorios
#os.chdir(r"C:\\Users\\andrea.garcia.ST\\Desktop\\Python\\Ejerc")
#os.getcwd()

date = np.load(files[0])
lat = np.load(files[1])
level = np.load(files[2])
lon = np.load(files[3])
P = np.load(files[4])
S = np.load(files[5])
T = np.load(files[6])


##2.2 Examine the shapes of T, S and P compared to lon, lat, date and level. 
#How do you think they are related?
T.shape
S.shape
P.shape

date.shape
lat.shape
level.shape
lon.shape

##2.3 Make a plot for each column of data in T, S and P (three plots).
#The vertical scale should be the levels data. Each plot should have a line for each column of data. It will look messy.
#figura = plt.figure()
#figura.clf()
#ax = figura.subplots(2,2, sharex=True)

plt.plot(T[0:], -level),{
    plt.title("T vs Depth"),
    plt.xlabel("T"),
    plt.ylabel("Depth")}

plt.plot(S[0:], -level),{
    plt.title("S vs Depth"),
    plt.xlabel("S"),
    plt.ylabel("Depth")}

plt.plot(P[0:], -level),{
    plt.title("P vs Depth"),
    plt.xlabel("P"),
    plt.ylabel("Depth")}

##2.4 Compute the mean and standard deviation of each of T, S and P at each depth in level.

#Este te lo hace solo de la primera fila
#np.nansum(T[0,])
#Pero así se hace de todas las filas (que son los niveles de profundidad)
#sumaT = np.nansum(T,axis=1)
mediaT = np.nanmean(T,axis=1)
desvT = np.nanstd(T,axis=1)

mediaS = np.nanmean(S,axis=1)
desvS = np.nanstd(S,axis=1)

mediaP = np.nanmean(P,axis=1)
desvP = np.nanstd(P,axis=1)

##2.5 Now make three similar plot, but show only the mean T, S and P at each depth. 
#Show error bars on each plot using the standard deviations

plt.plot(mediaT, -level),{
    plt.title("Media de T vs Depth"),
    plt.xlabel("Media T"),
    plt.ylabel("Depth")}
plt.errorbar(mediaT, -level, yerr = desvT)

plt.plot(mediaS, -level),{
    plt.title("Media de S vs Depth"),
    plt.xlabel("Media S"),
    plt.ylabel("Depth")}
plt.errorbar(mediaS, -level, yerr = desvS)

plt.plot(mediaP, -level),{
    plt.title("Media de P vs Depth"),
    plt.xlabel("Media T"),
    plt.ylabel("Depth")}
plt.errorbar(mediaP, -level, yerr = desvP)

##2.6 Account For Missing Data: Al hacerlo en spyder, tuve que hacerlo en el paso anterior. 
#Entiendo que en Jupyter no hace falta

##2.7 Create a scatter plot of the lon, lat positions of the ARGO float

plt.scatter(lon, lat)

