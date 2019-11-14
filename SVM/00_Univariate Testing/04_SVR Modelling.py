# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:18:44 2019

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
filepath = ('C:/Users/egwil/OneDrive/Desktop/Results/02_Deseasonalised 5 year avg - Processed.xlsx')
#sheetname = 'Sheet1'
#Import data 
df = pd.read_excel(filepath , parse_dates=['Current Date']) #sheet_name=sheetnamesheet_name=sheetname, 
df_filt =  (df['Current Date'] >= '2000-01-01')
df_filtered = df[df_filt]

"""
Step 3 -->Feature selection 
""" 

iterate = df_filtered.index.values.reshape(-1, 1)
x_values = df_filtered.iloc[:, 2:3]
#t_list =df.iloc[:, 0:1].index.tolist()  
#t_df = df.iloc[:, 0:1]
#test = pd.to_datetime(t_df.iloc[:, :].values.tolist())

print(iterate)

"""
Step 4 -->Setting window variables / dataframes
""" 

#Variables
start = 0
stop = 7
train = 8
wind_num = 1 
X_train = [[0],[1],[2],[3],[4],[5],[6]]

#blank data frames for appending 
df_test = pd.DataFrame(columns=['Window Number' , 'Window Values'])
df_pred_vals = pd.DataFrame(columns = ['Window Number', 'Test Value/s', 'Predict Value/s'])

"""
Step 5 -->Setting up sklearn : SVR 
""" 

from sklearn.svm import SVR
svregressor = SVR(kernel='rbf')
svregressor =  SVR(gamma ='auto')

"""
Step 6 -->Creating window and performing predictions
""" 
for i in iterate:
    while stop != 876: 
        wind_nam = 'w' + str(wind_num)
        temp = x_values[start:stop]
        wind_nam = np.array(temp)

        y_test = np.array(x_values[stop:train]).reshape(-1, 1)
        x_test = iterate[stop:train]  #.index.values.reshape(-1, 1) #np.array(train).reshape(-1, 1)
  
        svregressor.fit(X_train, wind_nam.ravel())

        y_pred = svregressor.predict(x_test)
        np_pred = np.array(y_pred)
        
        #exporting data to dataframe
        df_windows = pd.DataFrame({'Window Number' :wind_num, 'Window Values': wind_nam[:,0] })
        df_pred = pd.DataFrame({'Window Number' :wind_num,'Test Value/s' : [y_test], 'Predict Value/s': [np_pred]}) 

        #Counter
        start += 1 
        stop += 1
        train += 1
        wind_num += 1 
        
        #appending dataframe
        df_test = df_test.append(df_windows)
        df_pred_vals = df_pred_vals.append(df_pred)

"""
Step 7 -->Exporting data
""" 

df_test.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\New SVM Window Test Info.xlsx')
df_pred_vals.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\New SVM Window Test Results.xlsx')



"""
Step 3 --> Visualisation
""" 

#print(df_pred_vals)
#fig = plt.figure(1)
#ax1 = fig.add_subplot(111)
#ax1.set_xlabel('DateT')
#ax1.set_ylabel('MaxTemp (°C)')
#ax1.set_ylabel('MinTemp (°C)')
#ax1.set_title('Original Plot')
#ax1.plot('DateT','MaxTemp (°C)', data = df )
#
#plt.plot(X_test, y_pred, color = 'blue')
#plt.title('Original Plot')
#plt.xlabel(df.['DateT'])
#plt.ylabel(df.['MaxTemp (°C)'] , color = 'blue')
#plt.ylabel(dd.['MinTemp (°C)'], color = 'green')
#plt.show