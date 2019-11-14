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
from sklearn.metrics import confusion_matrix

"""
Step 2 --> Set variables
""" 

filepath = 'C:/Users/egwil/Dropbox/edwina/scratch/02_SVM/JHB Testing/000_Dataset/02_Deseasonalised 5 year avg - Processed JHB.xlsx'
#sheetname = 'Rainfall and Temperature'

"""
Step 2 -->Load dataset 
""" 

df = pd.read_excel(filepath)  #, sheet_name=sheetname)

"""
Step 3 --> subset selection
"""
#
df_features = df.loc[:,['Deseasonalised MaxTemp']].copy()
print(df_features)

"""
Step 4 --> Data exploration 
"""

#print(df_features.shape) 
#print(df_features.describe())

#"""
#Step 5 --> Data preprocessing 
#"""
##selecting the features
##X = df_features.drop('MaxTemp (°C)', axis=1)
##y = df_features['MaxTemp (°C)']
##
###Splitting the data for training and test
##from sklearn.model_selection import train_test_split
##X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
#
temp_dataholder = df_features.index.values.reshape(-1, 1)
X_train = temp_dataholder[0:5748]
y_train= df_features.iloc[:5748, -1:]

X_test = temp_dataholder[5748:7185]
y_test = df_features.iloc[5748:7185, -1:]

"""
#Step 6 --> Training and predicting 
"""

#Training model
from sklearn.svm import SVR
svregressor = SVR(kernel='rbf')
svregressor =  SVR(gamma ='auto')
svregressor.fit(X_train, y_train.values.ravel())

#making predictions
y_pred = svregressor.predict(X_test)


#Getting performance scores
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


print("Mean Absolute Error : ", mean_absolute_error(y_test,y_pred))
print("Mean Squared Error : ", mean_squared_error(y_test,y_pred))























##Converting features to dataframes
#p = pd.DataFrame(y_pred )
#ytrain = pd.DataFrame(y_train)
#ytest = pd.DataFrame(y_test)
#
##k = pd.DataFrame({'p':[ytest], 'l':[p]})
#print(p)
#print(df_pred)
        #appending dataframe
       # df_test = df_test.append(df_windows)
        #df_pred_vals = df_pred_vals.append(df_pred)
        
#print(df_test)
#print(df_pred_vals)
#df_windows = pd.DataFrame({'Window Number' :wind_num, 'Window Values': wind_nam[:,0] })
#df_pred = pd.DataFrame({'Test Value/s' : [y_test], 'Predict Value/s': [np_pred]}) #, })
        
#ytrain.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\21 Day ahead - SVM Window Training Data.xlsx', sheet_name = 'Training Values')
#ytest.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\21 Day ahead - SVM Window Testing Data.xlsx' , sheet_name = 'Test Values')
#p.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\21 Day ahead - SVM Window Test Results.xlsx', sheet_name = 'Predicted Values')
#print("Mean Absolute Error : ", mean_absolute_error(y_true,y_pred))
#print("Mean Squared Error : ", mean_squared_error(y_true,y_pred))
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

