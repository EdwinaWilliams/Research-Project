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

filepath = 'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/ModelTesting.xlsx'
sheetname = 'Train'
sheetname1 = 'Test'

"""
Step 2 -->Load dataset 
""" 

df = pd.read_excel(filepath, sheet_name=sheetname)


"""
Step 3 --> subset selection
"""

print(df.describe())
print(df)
#print(median)
#print(df_filt.head(20))

"""
Step 4 --> Train model and perform predictions uising Linear Regression 
"""

#X = df['Day'].values.reshape((-1,1))
#y = df["MaxTemp (°C)"].values.reshape((-1,1))
#
#print(X)
#print(y)

#iloc[:4, :1]
##split data into training and test set
from sklearn.model_selection import train_test_split
temp_dataholder = df.index.values.reshape(-1, 1)
X_train = temp_dataholder[0:30]
y_train= df.iloc[:30, -1:]
## 
X_test = temp_dataholder[30:31]
y_test = df.iloc[30:31:, -1:]


print('Training x variabes - Day')
print(X_train)
X_train_exp = pd.DataFrame(X_train)
X_train_exp.to_excel(r'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/ActualDataPoint.xlsx')
print('Training y variabes - MaxTemp')
print(y_train)
print('Testing x variabes - Day')
print(X_test)
print('Testing y variabes - MaxTemp(Actual)')
print(y_test)


#fit training data in linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predicting the Test set results
y_pred = regressor.predict(X_test)
print('Predicted day and predicted variable')
print(X_test, y_pred)
#Export results for further analysis

import xlsxwriter
workbook = xlsxwriter.Workbook('C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/Analysis.xlsx')

#starting from frist cell below headers
row = 1 
col = 0
worksheet_xdatapoints = workbook.add_worksheet('X_train')
worksheet_xdatavalues = workbook.add_worksheet('y_train')
worksheet_ydatapoints = workbook.add_worksheet('X_test')
worksheet_ydatavalues = workbook.add_worksheet('y_test')
worksheet_predvalues = workbook.add_worksheet('y_pred')

worksheet_xdatapoints.write(row, 2,'X_train')


workbook.close()
#"""
#Step 5 --> Evaluate model
#"""
##
##print(regressor.coef_)
##print(regressor.intercept_)
##
###calculate R squared 
#from sklearn.metrics import r2_score
#print('R squared')
#print(r2_score(y_test, y_pred))