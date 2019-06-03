# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:38:04 2019

@author: egwil
Title: Line plot - connected
Description: Line plot to visualize the time series 
Filters: StatName 
"""

"""
Step 1: Import libraries
"""

#import matplotlib for visualisations
from dateutil.parser import parse #use parser make the date colum to be parsed as a date field
import matplotlib as mpl
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
import numpy as np
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

"""
Step 2: Set variables 
"""

filepath = 'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/rainfall and temperature.xlsx'
sheetname = 'Rainfall and Temperature '
station = 'PRETORIA UNISA'
feature = 'MaxTemp (°C)'

"""
Step 3: Import as Dataframe
"""

df = pd.read_excel(filepath, sheet_name=sheetname, parse_dates = ['DateT'], index_col = 'DateT' )
df = df.loc[df.StasName == station, ['MaxTemp (°C)']]

print(df.head())

# Draw Plot
def plot_df(df, x, y, title="", xlabel='Year', ylabel=feature, dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

plot_df(df, x=df.index, y=df.loc[:,feature], title='Daily Temperatures in measured at the {} station from 1999 to 2018'.format(station))    

#df_filt = df.query('StasName == "PRETORIA UNISA"')
#X = df_filt.iloc[:, 3].values
#y = df_filt.iloc[:, 4].values
#
#
#plt.plot(X, y)
#plt.show()