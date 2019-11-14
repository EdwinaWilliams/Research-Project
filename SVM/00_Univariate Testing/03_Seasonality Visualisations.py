# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:08:03 2019

@author: egwil
"""

#Import libraries
from matplotlib import pyplot as plt
import pandas as pd  

#Importing data 
filepath = ('C:/Users/egwil/OneDrive/Desktop/Results/02_Deseasonalised 5 year avg - Processed.xlsx')

#Import data 
df = pd.read_excel(filepath)

df_filt =  (df['Current Date'] >= '2003-01-01')
df_filtered = df[df_filt]

print(df)

temperatures = df_filtered.iloc[:, 1:2].values
stationary_temp = df_filtered.iloc[:, 2:3].values
date = df_filtered.iloc[:, 0:1].values

plt.plot(date, temperatures, label="Actual Temperatures")
#plt.plot(date, stationary_temp, label = "Stationary Temperatures")
plt.legend(loc='top right', prop={'size': 15})

plt.title('Original Temperatures') #vs Stationary Temperatures')
plt.xlabel('Date')
plt.ylabel('Maximum Temperatures')
plt.show
#
#
#

##plt.plot(window, maxtemp, color = 'red')
#plt.legend(loc='top right')
#plt.title('Predictions vs Actual Values')
#plt.xlabel('Window')
#plt.ylabel('Maximum Temperatures')
#plt.show