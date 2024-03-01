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
fname = pooch.retrieve(
    "https://rabernat.github.io/research_computing/signif.txt.tsv.zip",
    known_hash='22b9f7045bf90fb99e14b95b24c81da3c52a0b4c79acf95d72fbe3a257001dbb',
    processor=pooch.Unzip()
)[0]

earthquakes = np.genfromtxt(fname, delimiter='\t')
depth = earthquakes[:, 8]
magnitude = earthquakes[:, 9]
latitude = earthquakes[:, 20]
longitude = earthquakes[:, 21]
####################
fig, ax = plt.subplots()

mapa = ax.scatter(longitude, latitude, c=earthquakes, s=magnitude)
fig.colorbar(mapa)
