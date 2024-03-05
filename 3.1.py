# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:59:59 2024
3.1 Assignment: Pandas Fundamentals with Earthquake Data
@author: andrea.garcia
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
#1) Use Pandas’ read_csv function directly on this URL to open it as a DataFrame

url = "http://www.ldeo.columbia.edu/~rpa/usgs_earthquakes_2014.csv"

df = pd.read_csv(url)

df.head(df)

#2) Re-read the data in such a way that all date columns are identified as dates
#and the earthquake ID is used as the index. Verify that this worked using the head and info functions.

#Poner columnas 0 y 12 como tiempo
df = pd.read_csv(url,
                 parse_dates=[0,12])
df.info()
#ID como índice
df = df.set_index('id')
df.head()

#3) Use describe to get the basic statistics of all the columns
#Note the highest and lowest magnitude of earthquakes in the database
##Lo que en Juppyter sale todo directamente, aqui tengo que meterlo en una variable para verlo
describe = df.describe()

#4)Use nlargest to get the top 20 earthquakes by magnitude
"""Como nlargest es para una serie, lo que hacemos es pasarle solo la columna, no el df entero.
Así obtenemos todos los datos del df. Dos maneras de hacerlo, la segunda para asegurarte de que
no saca terremotos con sitios que estén nulos"""
top20 = df.nlargest(20, 'mag')
top20=df[df['place'].notnull()].nlargest(20,'mag')

#Examine the structure of the place column. The state / country information seems to be in there.
#How would you get it out?
"""Aquí solo las columnas de place y magnitud, junto con el id (puesto como indice)"""
top20_2 = top20[['place','mag']]

#5)Extract the state or country using Pandas text data functions
#Add it as a new column to the dataframe called country. 
#Note that some of the “countries” are actually U.S. states.
"""Defino la nueva columna con df.country, paso la columna a dividir(place) y aplico método apply
con la funcion anonima lambda: Separa por coma y quedate con la segunda parte [1] 
cuando la separación sea mayor que 1"""
df['country'] = df['place'].apply(lambda x: x.split(', ')[1] 
                                  if len(x.split(', ')) > 1 
                                  else None)
#6)Display each unique value from the new column 
df.country.unique()

#7) Create a filtered dataset that only has earthquakes of magnitude 4 or larger
df_filtered = pd.DataFrame(df.loc[(df.mag>=4)])

#8)Using the filtered dataset (magnitude > 4), count the number of earthquakes in each country/state.
#Make a bar chart of this number for the top 5 locations with the most earthquakes
"""value_counts para la lista de todo el conteo"""
conteo_por_paises = df_filtered.country.value_counts()
"""Plotear"""
fig, ax = plt.subplots()
conteo_por_paises.nlargest(5).plot(kind='bar')
ax.set_xlabel("Country")
ax.set_ylabel("Number of earthquakes")
#ax.set_title("Top 5")

#9) Make a histogram the distribution of the Earthquake magnitudes

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)  # First subplot
plt.hist(df['mag'], bins=5, color='blue', alpha=0.7, log = True)
plt.title('Df total')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)  # Second subplot
plt.hist(df_filtered['mag'], bins=5, color='green', alpha=0.7, log = True)
plt.title('Df filtrado')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

#11)Visualize the locations of earthquakes by making a scatterplot of their latitude and longitude
#Use a two-column subplot with both the filtered and unfiltered datasets. Color the points by magnitude. Make it pretty
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)  # First subplot
plt.scatter(x = df.longitude, 
            y = df.latitude, 
            c=df.mag)
plt.title('Unfiltered')
plt.xlabel('Long')
plt.ylabel('Lat')
plt.grid()
plt.colorbar()


plt.subplot(1, 2, 2)  # Second subplot
plt.scatter(x = df_filtered.longitude, 
            y = df_filtered.latitude, 
            c=df_filtered.mag, 
            vmin=min(df.mag))
plt.title('Filtered')
plt.xlabel('Long')
plt.ylabel('Lat')
plt.grid()
plt.colorbar()

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

