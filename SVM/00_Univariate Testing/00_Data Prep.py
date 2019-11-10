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
#Set import variables
filepath = 'C:/Users/egwil/Dropbox/edwina/scratch/00_Data/rainfall and temperature.xlsx'
sheetname = 'Rainfall and Temperature'

#Import data -> setting index to date field
df = pd.read_excel(filepath, sheet_name=sheetname, parse_dates=['DateT'])

#1. Removed the data for other stations
#2. Removed data prior to 2002-01-01
""""
NOTE: The periods between 1999-01-01 till 2001-12-31
contains alot of missing months data 
removed the entire data between these values
"""
df_filt = (df['StasName'] == 'PRETORIA UNISA') & (df['DateT'] >= '2002-01-01')
df_filtered = df[df_filt]

#Creating new dataframe after data has been removed
df_new = df_filtered.set_index('DateT')

"""
Step 3 -->Interpolate dataset & Export
""" 

#Using the interpolate function
df_intplte = df_new.interpolate(method ='time')
print(df_intplte)

#Export results 
df_filtered.to_excel(r'C:\Users\egwil\Dropbox\edwina\scratch\02_SVM\Pretoria Testing\00_Original Dataset\00_Original Dataset.xlsx')
df_intplte.to_excel(r'C:\Users\egwil\Dropbox\edwina\scratch\02_SVM\Pretoria Testing\00_Original Dataset\01_Missing Values Replaced')

