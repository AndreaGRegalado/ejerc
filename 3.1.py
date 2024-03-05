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
#Como nlargest es para una serie, lo que hacemos es pasarle solo la columna, no el df entero
df.nlargest(20, ['mag'])

