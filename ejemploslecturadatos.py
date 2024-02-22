# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:23:49 2024

@author: andrea.garcia
"""

import xarray as xr
url_n = "http://iridl.ldeo.columbia.edu/expert/SOURCES/.NOAA/.NCEP/.CPC/.UNIFIED_PRCP/.GAUGE_BASED/.GLOBAL/.v1p0/.Monthly/.RETRO/.rain/dods"
# decode_times=False is required because the IRI Data Library uses non-standard encoding of times
ds = xr.open_dataset(url_n, decode_times=False)
print (ds)

import pandas as pd
url = "https://data.nasa.gov/api/views/gh4g-9sfh/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
print(df.head())