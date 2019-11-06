# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:00:36 2019

@author: egwil
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
#Set variables
filepath = 'C:/Users/egwil/Dropbox/edwina/scratch/00_Data/rainfall and temperature.xlsx'
sheetname = 'Rainfall and Temperature'
#Import data 
df = pd.read_excel(filepath, sheet_name=sheetname)
#print(df)
df_filt = df['StasName'] == 'PRETORIA UNISA'
df_filtered = df[df_filt]

temps = df_filtered.loc[:,['MaxTemp (°C)']].copy()

mark = temps['MaxTemp (°C)'].fillna(999.0)
mark.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\NullsMarked.xlsx')

################################################
#Getting null values
################################################

dfnulls = pd.read_excel('C:/Users/egwil/OneDrive/Desktop/Results/NullsMarked.xlsx')

df_filt1 = dfnulls['MaxTemp (°C)'] == 999.0
df_filtered1 = dfnulls[df_filt1]

temps1 = df_filtered1.loc[:,['MaxTemp (°C)']].copy()
index = temps1.index.values
#print(temps1)
#print(index)
#print(temps)
i_replace7 = (df.iloc[108510: 108511, 4].values  + df.iloc[108512: 108513   , 4].values)/2    
print(i_replace7)


for i in index:
    before = i -1 
    after = i + 1
    after_stop = i + 2
    count = 1
    
    while df.iloc[before:1,4] != None:
        if count != 10:
            before = before -1 
        else:
            datei = df.iloc[i:after, 3].values
            
        count += 1 
    while df.iloc[before:1,4] != None:
        if count != 10:
           after = after -1 
           after_stop = after_stop + 2
        else: 
            average last 5 years missing values if null
            1. date of missing value 
            2. Get each dates for the last 5 years
            3. Get the values for that 5 years --check
            4. Get average 
            
        count += 1 
            
    mean = (df.iloc[before:i, 4].values + df.iloc[after:after_stop, 4].values )/2
    tmp = df.iloc[i:after, 4].fillna(mean)
    print(i)
    print(mean)
    print(tmp)
    
    
#t = temps1.iloc[:6623, -1:]   

    