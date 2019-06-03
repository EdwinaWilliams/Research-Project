# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:38:04 2019

@author: egwil
"""

#import matplotlib for visualisations
import matplotlib.pyplot as plt 
import pandas as pd

# Load dataset 
# set dependent and independent variables 
filepath = 'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/rainfall and temperature.xlsx'
sheetname = 'Rainfall and Temperature '


df = pd.read_excel(filepath, sheet_name=sheetname)

df_filt = df.query('StasName == "PRETORIA UNISA"')
X = df_filt.iloc[:, 3].values
y = df_filt.iloc[:, 4].values


plt.plot(X, y)
plt.show()