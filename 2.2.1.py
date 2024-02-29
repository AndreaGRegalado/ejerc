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


#GridSpec(nrows, ncols, figure=None, left=None, bottom=None, right=None,
#top=None, wspace=None, hspace=None, width_ratios=None, height_ratios=None)
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
axes[0].grid(which='major',
             linestyle='--',
             color="black",
             linewidth=0.5)

fig.tight_layout()
plt.colorbar(mapa,
             label="ªC")

#axes[1].plot(lon, temp)
