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
import seaborn as sns 

"""
Step 2 --> Set variables
""" 

filepath = 'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/ModelTesting.xlsx'
sheetname = 'Train'

"""
Step 2 -->Load dataset 
""" 

df = pd.read_excel(filepath, sheet_name=sheetname)


"""
Step 3 --> subset selection
"""

temp_dataholder = df.index.values.reshape(-1, 1)
X_train = temp_dataholder[0:365]
y_train= df.iloc[:365, -1:]

X_test = temp_dataholder[365:366]
y_test = df.iloc[365:366, -1:]
#print(X_test)
#print(y_test)
"""
Step 4 --> Train model and perform predictions uising Linear Regression 
"""

#fit training data to linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor)

#Make preditions 
results = regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print('Test day: ' , X_test)
print('Test val: ' , y_test)
print('Predict val: ' , y_pred) 

#summarize the fit of the model
#

rss=((y_test-y_pred)**2).sum()
#mse=np.mean((y_test-y_pred)**2)
print("Final rmse value is =",np.sqrt(np.mean((y_test-y_pred)**2)))

#r_sq = regressor.score(X_train, y_train)
#mse = np.mean((y_pred-y_train)**2)
#print('Mean root squared error: ', mse)
#print('coefficient of determination:', r_sq)
#print('intercept:',regressor.intercept_)
#print('slope:', regressor.coef_)
#
#Plot data points on graph

plt.scatter(X_train, y_train)
plt.plot(X_test, y_test);
plt.show()

#Export results for further analysis

writer = pd.ExcelWriter('C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/Analysis.xlsx', engine='xlsxwriter')

data = {'Predict Day' : [X_test], 'Predict Values': [y_pred] }
columns = ['Predict Day','Predict Values']
index = ['1']

pred = pd.DataFrame(data, columns=columns, index=index)   

y_train.to_excel(writer, sheet_name = 'Training Datapoints')
y_test.to_excel(writer, sheet_name = 'Testing Datapoints')
pred.to_excel(writer, sheet_name = 'Predicted Values')
writer.save()
#
#
