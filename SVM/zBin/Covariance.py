# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:15:21 2019

@author: egwil
"""

import numpy as np 
import pandas as pd
filepath1 = 'C:/Users/egwil/Dropbox/edwina/scratch/02_SVM/JHB testing/000_Dataset/01_Missing Values Replaced.xlsx'
filepath2 = 'C:/Users/egwil/Dropbox/edwina/scratch/02_SVM/Pretoria Testing/000_Dataset/01_Missing Values Replaced.xlsx'

#Import data -> setting index to date field
df1 = pd.read_excel(filepath1)
df2 = pd.read_excel(filepath2)

#df_s1 =  (df['StasName'] >= 'PRETORIA UNISA')
#data1 = df[df_s1]
#
#df_s2 =  (df['StasName'] >= 'JHB BOT TUINE')
#data2 = df[df_s2]
print(df1['MaxTemp (°C)'])

covariance = np.cov(df1['MaxTemp (°C)'], df2['MaxTemp (°C)'])




