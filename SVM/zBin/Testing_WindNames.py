# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:19:05 2019

@author: egwil
"""

import sklearn as skl
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


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

df_7d = pd.read_excel(filepath, sheet_name=sheetname)

#plt.scatter(X_test,y_test, color = 'red')
#plt.plot(X_test, y_pred, color = 'blue')
#plt.title('SVR Regression Model')
#plt.xlabel('Days')
#plt.ylabel('Temperature - Max')
#plt.show