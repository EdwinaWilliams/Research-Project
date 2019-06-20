# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 05:32:23 2019

@author: egwil
"""


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#dataset loading 
filepath = 'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/ModelTesting.xlsx'
sheetname1 = 'Train'
sheetname2 = 'Test'


"""
Step 2 -->Load dataset 
""" 


#train dataset 
train_data = pd.read_excel(filepath, sheet_name=sheetname1, index_col ='Day' )
#removing Nan if any in dataset 
#train_data = train_data.dropna()
#train dataset
test_data = pd.read_excel(filepath, sheet_name=sheetname2, index_col ='Day')
#removing Nan if any in dataset 
#test_data= test_data.dropna()
#loading the data in numpy matrix 
X = train_data.loc
y = train_data.iloc['MaxTemp (°C)']
x_test = test_data.loc
y_test = test_data.iloc['MaxTemp (°C)']

print(X)
print(y)
print(x_test)
print(y_test)
##initialisation of linear regression 
#linear_model = LinearRegression()
##inserting the train data in model for training purpose 
#linear_model.fit(X,y)
##now model trained with this data
##now we will do prediction for the data 
#y_pred = linear_model.predict(x_test)
##test our result how accurate our model is 
#error = y_test-y_pred
##e= np.sum(error)
##abserror = np.absolute(error)
##sqrarr= np.square(error)
##addall= np.sum(sqrarr)
#print('Coefficients: \n', linear_model.coef_)
#print("Mean squared error: %.2f"
#      % mean_squared_error(y_test, y_pred))
#print(r2_score(y_test,y_pred))
##ploting the dataset
##for ploting the data  for train data
#plt.scatter(X,y,color='red')
#plt.title(" train data set ")
#plt.xlabel("X")
#plt.ylabel("Y")
#plt.show()
#
##for ploting the data  for test data with predicted data 
#plt.scatter(x_test,y_test,color='red')
#plt.plot(x_test,y_pred,color='blue')
#plt.title(" (Test data set)")
#plt.xlabel("X")
#plt.ylabel("Y")
#plt.show()
