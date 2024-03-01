# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:51:38 2024
Ejercicio More Matplotlib - Line Plots
@author: andrea.garcia
"""
##Problem 1: Line plots

#####################
import pooch
POOCH = pooch.create(
    path=pooch.os_cache("noaa-data"),
    # Use the figshare DOI
    base_url="doi:10.5281/zenodo.5553029/",
    registry={
        "HEADERS.txt": "md5:2a306ca225fe3ccb72a98953ded2f536",
        "CRND0103-2016-NY_Millbrook_3_W.txt": "md5:eb69811d14d0573ffa69f70dd9c768d9",
        "CRND0103-2017-NY_Millbrook_3_W.txt": "md5:b911da727ba1bdf26a34a775f25d1088",
        "CRND0103-2018-NY_Millbrook_3_W.txt": "md5:5b61bc687261596eba83801d7080dc56",
        "CRND0103-2019-NY_Millbrook_3_W.txt": "md5:9b814430612cd8a770b72020ca4f2b7d",
        "CRND0103-2020-NY_Millbrook_3_W.txt": "md5:cd8de6d5445024ce35fcaafa9b0e7b64"
    },
)


import pandas as pd

with open(POOCH.fetch("HEADERS.txt")) as fp:
    data = fp.read()
lines = data.split('\n')
headers = lines[1].split(' ')

dframes = []
for year in range(2016, 2019):
    fname = f'CRND0103-{year}-NY_Millbrook_3_W.txt'               
    df = pd.read_csv(POOCH.fetch(fname), parse_dates=[1],
                     names=headers, header=None, sep='\s+',
                     na_values=[-9999.0, -99.0])
    dframes.append(df)

df = pd.concat(dframes)
df = df.set_index('LST_DATE')
df

#########################################################
#### BELOW ARE THE VARIABLES YOU SHOULD USE IN THE PLOTS!
#### (numpy arrays)  
#### NO PANDAS ALLOWED!
#########################################################

t_daily_min = df.T_DAILY_MIN.values
t_daily_max = df.T_DAILY_MAX.values
t_daily_mean = df.T_DAILY_MEAN.values
p_daily_calc = df.P_DAILY_CALC.values
soil_moisture_5 = df.SOIL_MOISTURE_5_DAILY.values
soil_moisture_10 = df.SOIL_MOISTURE_10_DAILY.values
soil_moisture_20 = df.SOIL_MOISTURE_20_DAILY.values
soil_moisture_50 = df.SOIL_MOISTURE_50_DAILY.values
soil_moisture_100 = df.SOIL_MOISTURE_100_DAILY.values
date = df.index.values

units = lines[2].split(' ')
for name, unit in zip(headers, units):
    print(f'{name}: {unit}')
############################################################################################

#3 GRAFICAS EN VERTICAL
from matplotlib import pyplot as plt

fig, axes = plt.subplots(figsize=(12, 10),nrows=3) 

#Primera gráfica (axes[0])
##Datos a representar, color de media y etiqueta para la leyenda
axes[0].plot(date, t_daily_mean, 
             color= "#bf00bf",
             label= "Daily mean")
##Relleno de los máximos y minimos, con su color, distancia y etiqueta para la leyenda
axes[0].fill_between(date, t_daily_max, t_daily_min,
                     color="#CBC5C3", 
                     alpha=0.5, 
                     label="Daily range")
##Añadir leyenda, la localización 1 es arriba a la derecha, y tamaño de letra
axes[0].legend(loc=1,
               fontsize=8)
##Nombre eje y, tamaño de letra
axes[0].set_ylabel(ylabel="Temperature [ºC]",
                   fontsize=11)
##Grid del fondo, tipo y tamaño de línea
axes[0].grid(which='major',
             linestyle='--',
             linewidth=0.75)
##Ajuste al minimo y máximo de datos fecha
axes[0].set_xlim(left= min(date), right= max(date))


#Segunda gráfica
axes[1].plot(date, p_daily_calc)
axes[1].set_ylabel(ylabel="Precipitation [mm/day]",
                   fontsize=11)

#axes[1].get_xaxis().set_visible(False)
axes[1].grid(which='major',
             linestyle='--',
             linewidth=0.75)
axes[1].set_xlim(left= min(date), right= max(date))
axes[1].set_ylim([0,70])

#Tercera gráfica
axes[2].plot(date, soil_moisture_5,
             label="5 cm")
axes[2].plot(date, soil_moisture_10,
             label="10 cm")
axes[2].plot(date, soil_moisture_20,
             label="20 cm")
axes[2].plot(date, soil_moisture_50,
             label="50 cm")
axes[2].plot(date, soil_moisture_100,
             label="100 cm")
axes[2].legend(loc=3,
               fontsize=7)
axes[2].grid(which='major',
             linestyle='--',
             linewidth=0.75)
axes[2].set_ylabel(ylabel="Soil Moisure [$m^{3}m^{3}$]",
                   fontsize=11)

axes[2].set_xlim(left= min(date), right= max(date))
axes[2].set_ylim([0.01,0.34])

#Para quitar las fechas de los ejes x de las dos primeras gráficas sin quitar el grid
for ax in axes:
    ax.grid(True)
    ax.label_outer()
#Poner el nombre del eje x solo en la última
plt.xlabel("Date")

