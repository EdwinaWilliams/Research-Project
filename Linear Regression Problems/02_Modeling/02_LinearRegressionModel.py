# -*- coding: utf-8 -*-
"""
Spyder Editor

This script file is used for a linear regression model using sklearn, pandas, matplotlib, pandas and seaborn.

Script steps:
1# Import and analyze data  
2# Data preprocessing (filtering and handling missing values)
2# Solve and see how valid solution is
"""

"""
Step 1 --> Import libraries
"""

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns #works with matplot lib have to import together ??

"""
Step 2 --> Set variables
""" 

filepath = 'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/rainfall and temperature.xlsx'
sheetname = 'Rainfall and Temperature '
cols = ['DateT','MaxTemp (°C)']
start_date = '1999/01/01'
end_date = '1999/01/02'

"""
Step 2 -->Load dataset 
""" 

df = pd.read_excel(filepath, sheet_name=sheetname)

#making sure that the date field is date format
df['DateT'] = pd.to_datetime(df['DateT'])
mask = (df['DateT'] > start_date) & (df['DateT'] <= end_date)
location = (df['StasName'] == "PRETORIA UNISA")
df=df.loc[mask]
df_new=df.loc[location]
print(df)
print(df_new)
"""
Step 3 --> subset selection
"""
##filter data
#df_filt = df.loc[["PRETORIA UNISA"],["MaxTemp (°C)"]]
## Identify missing values 
#print(df_filt['MaxTemp (°C)'].isnull()) 
#
##count amount of missing values 
#print(df_filt.isnull().sum())
#
##Replace missing values 
## True = Missing 
#median = float(df_filt['MaxTemp (°C)'].median())
#df_filt['MaxTemp (°C)'].fillna(median, inplace=True)
#
#print(df_filt.describe())
##print(median)
##print(df_filt.head(20))
#
#"""
#Step 4 --> Train model and perform predictions uising Linear Regression 
#"""
## convert date to numerical value
##import datetime as dt
##df_filt['DateT'] = pd.to_datetime(df_filt['DateT'])
##df_filt['DateT']=df_filt['DateT'].map(dt.datetime.toordinal)
## set dependent and independent variables 
#X = df_filt["MaxTemp (°C)"].values.reshape((-1,1))
#y = df_filt["MaxTemp (°C)"].values
#
##split data into training and test set
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)
#
#print(X_train)
#print(y_train)

#fit training data in linear regression model
#from sklearn.linear_model import LinearRegression
#regressor = LinearRegression()
#regressor.fit(X_train, y_train)

# predicting the Test set results
#y_pred = regressor.predict(X_test)
#print(y_pred)

"""
Step 5 --> Evaluate model
"""
#
#print(regressor.coef_)
#print(regressor.intercept_)
#
##calculate R squared 
#from sklearn.metrics import r2_score
#print(r2_score(y_test, y_pred))