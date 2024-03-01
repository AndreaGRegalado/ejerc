# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 12:33:48 2024
Ejercicio More Matplotlib - Contour Map
@author: andrea.garcia
"""
######################################
import xarray as xr
ds_url = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Diagnostic/.surface/.temp/dods'
ds = xr.open_dataset(ds_url, decode_times=False)

#########################################################
#### BELOW ARE THE VARIABLES YOU SHOULD USE IN THE PLOTS!
#### (numpy arrays) 
#### NO XARRAY ALLOWED!
#########################################################

temp = ds.temp[-1].values - 273.15
lon = ds.X.values
lat = ds.Y.values
######################################

from matplotlib import pyplot as plt
<<<<<<< HEAD
=======
import numpy as np
>>>>>>> b2bc8a8aa32d4d51c9218d6ecf26f27bbd0a5bc1


#GridSpec(nrows, ncols, figure=None, left=None, bottom=None, right=None,
#top=None, wspace=None, hspace=None, width_ratios=None, height_ratios=None)
<<<<<<< HEAD
fig, axes = plt.subplots(figsize=(12, 10), nrows = 1, ncols = 2, gridspec_kw={'width_ratios': [5, 2],
                                            "wspace":0})
#fig, axes = plt.subplots(figsize=(12, 10),nrows=3) 
#Mapa
mapa = axes[0].contourf(lon, lat, temp, 
                        cmap='magma', 
                        extend='both')
axes[0].set_title("Current Global Temperature",
                  fontsize=8)
axes[0].set_xlabel(xlabel="Longitude",
                   fontsize=8)
axes[0].set_ylabel(ylabel="Latitude",
                   fontsize=8)
=======
fig, axes = plt.subplots(figsize=(15, 5), nrows = 1, ncols = 2, gridspec_kw={'width_ratios': [5, 1],
                                            "wspace":0.0025})
#fig, axes = plt.subplots(figsize=(12, 10),nrows=3) 
#Mapa
mapa = axes[0].contourf(lon, lat, temp, 
                        cmap='magma',
                        levels=20,
                        extend='both')
axes[0].contour(lon,lat,temp>0,
                cmap="binary")
axes[0].set_title("Current Global Temperature"
                  )
axes[0].set_xlabel(xlabel="Longitude",
                   fontsize=13)
axes[0].set_ylabel(ylabel="Latitude",
                   fontsize=13)
>>>>>>> b2bc8a8aa32d4d51c9218d6ecf26f27bbd0a5bc1
axes[0].grid(which='major',
             linestyle='--',
             color="black",
             linewidth=0.5)

<<<<<<< HEAD
fig.tight_layout()
plt.colorbar(mapa,
             label="ªC")

#axes[1].plot(lon, temp)
=======
#fig.tight_layout()
plt.colorbar(mapa,
             label="ªC",
             shrink=0.5)

media_por_latitud = np.mean(temp, axis=1)

axes[1].plot(media_por_latitud,lat,
             color="black",
             linewidth=2)
axes[1].set_title("Zonal Mean Temperature")
axes[1].grid(which='major',
             linestyle='--',
             color="black",
             linewidth=0.5)
axes[1].set_xlim(-30, 30)
axes[1].set_ylim([-90,90])
>>>>>>> b2bc8a8aa32d4d51c9218d6ecf26f27bbd0a5bc1
