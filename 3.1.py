# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:59:59 2024
3.1 Assignment: Pandas Fundamentals with Earthquake Data
@author: andrea.garcia
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
#1. Use Pandas’ read_csv function directly on this URL to open it as a DataFrame

url = "http://www.ldeo.columbia.edu/~rpa/usgs_earthquakes_2014.csv"

df = pd.read_csv(url)

df.head(df)