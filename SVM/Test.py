# -*- coding: utf-8 -*-
"""
Removing trend and seasonality
"""

"""
Step 1 --> Import libraries
"""
import sklearn as skl
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

"""
Step 2 -->Load dataset 
""" 
#Step 2 --> Set variables
filepath = 'C:/Users/egwil/Dropbox/edwina/scratch/00_Data/rainfall and temperature.xlsx'
sheetname = 'Rainfall and Temperature'
#Import data 
df = pd.read_excel(filepath, sheet_name=sheetname)

"""
Step 3 --> Data preparation 
"""
#Filtering for specific station 
df_filt = df['StasName'] == 'PRETORIA UNISA'
df_filtered = df[df_filt]
df_filtered = df_filtered.dropna()
#print(df_filtered)

temp_dataholder = df_filtered.index.values.reshape(-1, 1)
day =df_filtered.iloc[:, 3:4] #temp_dataholder[0:365]
temps= df_filtered.iloc[:, 4:5]

print(day)
#print(y_train)


plt.plot(day, temps, color = 'blue')
plt.title('First Year Temperatures')
plt.xlabel('Day')
plt.ylabel('Temperature - Max')
plt.show