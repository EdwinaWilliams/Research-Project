# -*- coding: utf-8 -*-
"""
Removing trend and seasonality
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
#Step 2 --> Set variables
filepath = 'C:/Users/egwil/OneDrive/Desktop/Results/Deseasonalised Temperature Data Pretoria.xlsx'
#sheetname = 'Rainfall and Temperature'
#Import data 
df = pd.read_excel(filepath)  #, sheet_name=sheetname)

temps = df.dropna()

#print(temps)

temp_dataholder = temps.index.values.reshape(-1, 1)
X_train = temp_dataholder[0:365]
y_train= temps.iloc[:365, -1:]

X_test = temp_dataholder[365:366]
y_test = temps.iloc[365:366, -1:]

print(y_train)
#print(y_train)
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
print('Position Number : ', X_test)
print('Actual value : ' , y_test)
print('Predicted value : ', y_pred)