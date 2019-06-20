# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:15:31 2019

@author: egwil
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:38:04 2019

@author: egwil
Title: Line plot - connected
Description: Line plot to visualize the time series 
Filters: StatName 
"""

"""
Step 1: Import libraries
"""

#import matplotlib for visualisations
from dateutil.parser import parse #use parser make the date colum to be parsed as a date field
import matplotlib as plt
from mlxtend.plotting import plot_linear_regression 
import pandas as pd
import seaborn as sns
import numpy as np


"""
Step 2 --> Set variables
""" 

filepath = 'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/ModelTesting.xlsx'
sheetname = 'Train'

"""
Step 2 -->Load dataset 
""" 

df = pd.read_excel(filepath, sheet_name=sheetname)

temp_dataholder = df.index.values.reshape(-1, 1)
#X_tmp = 
X = np.array(temp_dataholder[0:6])
y = np.array(df.iloc[:6, -1:])
#y = np.array([df.values('MaxTemp (°C)')])

print(X,y)

intercept, slope, corr_coeff = plot_linear_regression(X, y)
plt.show()