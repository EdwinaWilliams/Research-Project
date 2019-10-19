# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:53:31 2019

@author: egwil
"""

"""
Step 1 --> Import libraries
"""
import sklearn as skl
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import xlsxwriter 
  

#Create workbook for saving results 
#workbook = xlsxwriter.Workbook('C:/Users/egwil/OneDrive/Desktop/Results/SVM_sw_results.xlsx')
#worksheet = workbook.add_worksheet('sheet')
#worksheet.cell(row=1, column=1).value='Window_number'

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
#Getting desired feature
temps = df_filtered.loc[:,['MaxTemp (°C)']].copy()
#Removing nan values from dataset
temps = temps.dropna()

temps =temps.iloc[:6623, -1:].values.tolist()  #to_dict()
#windows =  temps.rolling(5).sum() 

#temps = df[temps]
print(temps)
#print(windows)

start = 0
stop = 10
train = 11
wind_num = 1 
X_train = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]

from sklearn.svm import SVR
svregressor = SVR(kernel='rbf')
svregressor =  SVR(gamma ='auto')
#balnk data frames for appending 
df_test = pd.DataFrame(columns=['Window Number' , 'Window Values'])
df_pred_vals = pd.DataFrame(columns = ['Window Number', 'Test Value/s', 'Predict Value/s'])
#Creating windows and performing predictions
for i in temps:
    while stop != 662: 
        wind_nam = 'w' + str(wind_num)
        temp = temps[start:stop]
        wind_nam = np.array(temp)
        #print(wind_nam)
        #while train != 10:
        y_test = np.array(temps[stop:train]).reshape(-1, 1)
        x_test = np.array(train).reshape(-1, 1)
        svregressor.fit(X_train, wind_nam.ravel())

        y_pred = svregressor.predict(x_test)
        np_pred = np.array(y_pred)
        error = y_test- y_pred
        error_abs = abs(y_test)- abs(y_pred)
        #exporting data to dataframe
        df_windows = pd.DataFrame({'Window Number' :wind_num, 'Window Values': wind_nam[:,0] })
        df_pred = pd.DataFrame({'Window Number' :wind_num,'Test Value/s' : [y_test], 'Predict Value/s': [np_pred]}) 

        start += 1 
        stop += 1
        train += 1
        wind_num += 1 
        #appending dataframe
        df_test = df_test.append(df_windows)
        df_pred_vals = df_pred_vals.append(df_pred)
        
#print(df_test)
#print(df_pred_vals)
#df_windows = pd.DataFrame({'Window Number' :wind_num, 'Window Values': wind_nam[:,0] })
#df_pred = pd.DataFrame({'Test Value/s' : [y_test], 'Predict Value/s': [np_pred]}) #, })
        
df_test.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\SVM Window Test Info.xlsx')
df_pred_vals.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\SVM Window Test Results.xlsx')
