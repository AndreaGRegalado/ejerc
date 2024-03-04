# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:10:32 2024
Ejer3 - Scatter Plots
@author: andrea.garcia
"""
###################
from matplotlib import pyplot as plt
import numpy as np
import pooch
import matplotlib.colors


fname = pooch.retrieve(
    "https://rabernat.github.io/research_computing/signif.txt.tsv.zip",
    known_hash='22b9f7045bf90fb99e14b95b24c81da3c52a0b4c79acf95d72fbe3a257001dbb',
    processor=pooch.Unzip())[0]

earthquakes = np.genfromtxt(fname, delimiter='\t')
depth = earthquakes[:, 8]
magnitude = earthquakes[:, 9]
latitude = earthquakes[:, 20]
longitude = earthquakes[:, 21]
####################
#Monto la figura, con esas medidas
fig, ax = plt.subplots(figsize=(15, 8))
#Tamaño de los circulos atendiendo a la magnitud
sizes=magnitude**4/100
#Monto mapa, con tamaño circulos y colores de profundidad, la escala logaritmica no me salió
mapa = ax.scatter(longitude, latitude, s=sizes, c=np.log10(depth),
                  norm=matplotlib.colors.LogNorm())
#Barra de escala
fig.colorbar(mapa,
             label="Depth[m]")
ax.set_title("Location of Significant Earthquakes with size indicating relative magnitude")
ax.set_xlabel(xlabel="Longitude(°)")
ax.set_ylabel(ylabel="Latitude (°)")
ax.grid(which='major',
             color="grey",
             linewidth=0.5)


