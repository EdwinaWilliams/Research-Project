# -*- coding: utf-8 -*-
"""
Spyder Editor

This script file is used to check for missing values and replace these values with the median value.
"""

"""
Step 1 --> Import libraries
"""
from sklearn.datasets import load_iris

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

"""
Step 2 --> Set variables
""" 

filepath = 'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/rainfall and temperature.xlsx'
sheetname = 'Rainfall and Temperature '
cols = ['DateT','MaxTemp (°C)']

"""
Step 3 --> Load dataset 
""" 

df = pd.read_excel(filepath, sheet_name=sheetname, index_col="StasName")

"""
Step 3 --> Subset selection
"""
#station = PRETORIA UNISA
df_filt = df.loc[["PRETORIA UNISA"],["DateT","MaxTemp (°C)"]]

"""
Step 4 --> Analyze data selection for missing value  
"""

#getting the data description
print(df_filt.describe())

# Identify missing values 
print(df_filt['MaxTemp (°C)'].isnull()) 

#count amount of missing values 

print(df_filt.isnull().sum())

"""
Step 5 --> Replace missing value with median
"""
# True = Missing 
median = df_filt['MaxTemp (°C)'].median()
df_filt['MaxTemp (°C)'].fillna(median, inplace=True)

# Identify missing values 
print(df_filt['MaxTemp (°C)'].isnull()) 

#count amount of missing values 

print(df_filt.isnull().sum())