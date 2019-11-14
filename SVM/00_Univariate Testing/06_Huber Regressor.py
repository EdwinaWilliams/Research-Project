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
df_filt =  (df['Current Date'] >= '2003-01-01')
df_filtered = df[df_filt]


print(df_filtered)

from sklearn.linear_model import HuberRegressor, LinearRegression
from sklearn.datasets import make_regression

X_tmp = df_filtered.index.values.reshape(-1, 1)
X = X_tmp[:]
y = df_filtered.iloc[:, 2:3] #[:4] = rng.uniform(10, 20,4)

huber = HuberRegressor().fit(X, y.values.ravel())

print(huber.score(X, y) )

huber.predict(X[:1, ])

print("Huber coefficients:", huber.coef_)
