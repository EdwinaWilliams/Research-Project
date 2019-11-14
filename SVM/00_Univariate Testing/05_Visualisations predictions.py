# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:08:03 2019

@author: egwil
"""

#Import libraries
from matplotlib import pyplot as plt
import pandas as pd  

plt.rcParams.update({'font.size': 22})
#Importing data 
filepath = ('C:/Users/egwil/OneDrive/Desktop/Results/New SVM Window Test Results Formatted.xlsx')

#Import data 
df = pd.read_excel(filepath)

#print(df)

maxtemp_actual = df.iloc[:, 1:2].values
maxtemp_pred = df.iloc[:, 2:3].values
window = df.iloc[:, 0:1].values

#print(maxtemp_pred)

plt.plot(window, maxtemp_actual, label="Actual Value")
plt.plot(window, maxtemp_pred, label = "Predicted Value")
#plt.plot(window, maxtemp, color = 'red')
plt.legend(loc='top right', prop={'size': 22})
plt.title('Predictions vs Actual Values')
plt.xlabel('Window')
plt.ylabel('Maximum Temperatures')
plt.show


#Getting performance scores
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

y_true = df.iloc[:,1:2 ]
y_pred = df.iloc[:, 2:3]

print("Mean Absolute Error : ", mean_absolute_error(y_true,y_pred))
print("Mean Squared Error : ", mean_squared_error(y_true,y_pred))