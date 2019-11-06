# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:27:48 2019

@author: egwil
"""
import pandas as pd 
from matplotlib import pyplot
#Step 1 --> Load data 
filepath = 'C:/Users/egwil/Dropbox/edwina/scratch/00_Data/rainfall and temperature.xlsx'
sheetname = 'Rainfall and Temperature'
df = pd.read_excel(filepath, sheet_name=sheetname, index_col = 3)
df_filt = df['StasName'] == 'PRETORIA UNISA'
df_filtered = df[df_filt]
dataset = df_filtered.iloc[:, 3:4]

X = dataset.values 

#Step 2 --> create a differenced series

diff = list()
days_in_year = 365

#Code for removing seasonality using daily temperatures
#5 Leap years fall in period 1991 - 2018 --> result in incorrect days offsetting each other 
'''
for i in range(days_in_year, len(X)):
    value = X[i] - X[i - days_in_year]
    diff.append(value)
pyplot.plot(diff)
pyplot.show()
'''
#Getting the monthly mean
#resample = dataset.resample('M')
#monthly_mean = resample.mean()
#print(monthly_mean.head(13))
#monthly_mean.plot()
#pyplot.show()

#Differencing based on monthly means
#resample = dataset.resample('M')
#monthly_mean = resample.mean()
#X = dataset.values
#diff = list()
#months_in_year = 12
#for i in range(months_in_year, len(monthly_mean)):
#	value = monthly_mean[i] - monthly_mean[i - months_in_year]
#	diff.append(value)
#pyplot.plot(diff)
#pyplot.show()

#Code for removing seasonality using monthly average 
#Note GAPs are identified between each year need to investigate why 


for i in range(days_in_year, len(X)):
    month_str = str(dataset.index[i].year-1)+'-'+ str(dataset.index[i].month)
    month_mean_last_year = dataset[month_str].mean()
    value = X[i] - month_mean_last_year
    diff.append(value)
    
with open("file.txt", "w") as output:
    output.write(str(diff))


print(diff)
pyplot.plot(diff)
pyplot.show()