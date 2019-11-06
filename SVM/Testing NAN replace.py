# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:18:58 2019

@author: egwil
"""

"""
Step 1 --> Import libraries
"""
import sklearn as skl
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd  
import datetime as dt
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
fok = temps.reset_index()
print(fok)
mark = temps['MaxTemp (°C)'].fillna(999.0)
mark.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\NullsMarked.xlsx')

################################################
#Getting null values
################################################

dfnulls = pd.read_excel('C:/Users/egwil/OneDrive/Desktop/Results/NullsMarked.xlsx')

df_filt1 = dfnulls['MaxTemp (°C)'] == 999.0
df_filtered1 = dfnulls[df_filt1]

temps1 = df_filtered1.loc[:,['MaxTemp (°C)']].copy()
index = temps1.index.values.tolist()
#print(index)

################################################
#Replacing null values
################################################

for i in index:
    before = i - 1 
    after = i + 1
    after_stop = i + 2
    count = 1
    #checking before list to make sure it's not in the list 
    if before in index: #1st check
        before = before - 1
        if before in index: #2nd index check
            before = before -1 
            if before in index: #3rd index check 
                before = before -1         
    else: 
        before ="tsek"
        
print(i)       
print(before)
#    if pd.isnull(df.iloc[before:i,4]):
#        while count != 5:
#            before = before - 1
#            if pd.isnull(df.iloc[before:i, 4]):
#                count += 1
#            else:
#                break 
#    print(before)
     
            
            
            
            
            