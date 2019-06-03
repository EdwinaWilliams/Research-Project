# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:15:31 2019

@author: egwil
"""

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
#df.reset_index(inplace=True)

df = df.loc[df.StasName == station, ['MaxTemp (°C)']]

"""
Step 4: Prepare data 
"""

df['year'] = df.index.year
df['month'] = df.index.month
years = df['year'].unique()

print(df.head())


# Prep Colors
np.random.seed(100)
mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(years), replace=False)

# Draw Plot
plt.figure(figsize=(16,12), dpi= 80)
for i, y in enumerate(years):
    if i > 0:        
        plt.plot('month', 'MaxTemp (°C)', data=df.loc[df.year==y, :], color=mycolors[i], label=y)
        plt.text(df.loc[df.year==y, :].shape[0]-.9, df.loc[df.year==y, 'MaxTemp (°C)'][-1:].values[0], y, fontsize=12, color=mycolors[i])
        
# Decoration
plt.gca().set(xlim=(-0.3, 11), ylim=(2, 30), ylabel='MaxTemp (°C)', xlabel='Month')
plt.yticks(fontsize=12, alpha=.7)
plt.title("Seasonal Plot of Temperature Time Series", fontsize=20)
plt.show()     