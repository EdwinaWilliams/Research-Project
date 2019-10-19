# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 23:18:10 2019

@author: egwil
"""

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
import sklearn as skl
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import cvxopt
from sklearn.metrics import confusion_matrix

"""
Step 2 --> Set variables
""" 

filepath = 'C:/Users/egwil/Dropbox/edwina/scratch/00_Data/rainfall and temperature.xlsx'
sheetname = 'Rainfall and Temperature'

"""
Step 2 -->Load dataset 
""" 

df = pd.read_excel(filepath, sheet_name=sheetname)

"""
Step 3 --> subset selection
"""

#Filtering for specific station 
df_filter = df['StasName'] == 'PRETORIA UNISA'
df_filtered = df[df_filter]

#Getting desired feature

df_features = df_filtered.loc[:,['MaxTemp (°C)']].copy()
#Removing nan values from dataset
df_features = df_features.dropna()
#df_features['ID'] = range(1, len(df_features) + 1)
#print(df_feat.head(5))

df_features.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\Full Features.xlsx')

"""
Step 4 --> Data exploration 
"""

print(df_features.shape) 
print(df_features.describe())

"""
Step 5 --> Data preprocessing 
"""
#selecting the features
#X = df_features.drop('MaxTemp (°C)', axis=1)
#y = df_features['MaxTemp (°C)']
#
##Splitting the data for training and test
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

#Setup window 

window = df_features.rolling(2).mean().shift()

temp_dataholder = df_features.index.values.reshape(-1, 1)
X_train = temp_dataholder[0:7]
y_train= df_features.iloc[:7, -1:]

X_test = temp_dataholder[7:8]
y_test = df_features.iloc[7:8, -1:]


"""
#Step 6 --> Training and predicting 
"""
#Training model
from sklearn.svm import SVR
svregressor = SVR(kernel='rbf')
svregressor =  SVR(gamma ='auto')


for window in windows:
    svregressor.fit(X_train, y_train.values.ravel())
    y_pred = svregressor.predict(X_test)
    return abs(y_pred) - abs(y_test) 

#(self, 5m min_periods=None, center = False, win_type = None, on = None, closed= None )



#
##making predictions

#print(X_test)
#print(y_test)
#print(y_pred)
#
##saving results to file 
#result_df = pd.DataFrame()
#
#
##result_df['ID'] = 
#
#result_df['Predictions']= y_pred
#result_df.set_index(X_test)
#result_df['Actual'] = y_test
#
#result_df.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\Test Results.xlsx')
##
##print(result_df.head())
##Put in step to visualize results 
#"""
#Step 7 --> Evaluate
#"""
#
#MAE
#from sklearn.metrics import mean_absolute_error
#mae = mean_absolute_error(y_test, y_pred)
#print('MAE = ', mae)
#
##MSE
#from sklearn.metrics import mean_squared_error
#mse = mean_squared_error(y_test, y_pred)
#print('MSE = ',mse)
#
##RMSE
#from math import sqrt
#rmse = sqrt(mse)
#print('RMSE = ',rmse)
#
##Visualisations 
#plt.scatter(X_test,y_test, color = 'red')
#plt.plot(X_test, y_pred, color = 'blue')
#plt.title('SVR Regression Model')
#plt.xlabel('Days')
#plt.ylabel('Temperature - Max')
#plt.show

