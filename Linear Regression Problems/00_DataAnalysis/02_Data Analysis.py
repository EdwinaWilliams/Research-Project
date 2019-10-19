# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 22:33:27 2019

@author: Edwina WIlliams 

"""

"""
Step 1 --> Import libraries
"""

import numpy as np
import pandas as pd

"""
Step 2 --> Set variables
""" 

filepath = 'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/rainfall and temperature.xlsx'
sheetname = 'Rainfall and Temperature '

"""
Step 2 -->Load dataset 
""" 

df = pd.read_excel(filepath, sheet_name=sheetname)
#df2 = pd.DataFrame(group.describe().rename(columns={'MaxTemp (°C)':name}).squeeze()
#                         for name, group in df.groupby('StasName'))
print(df.head(20))
#print(df.groupby('StasName').describe().unstack(1))

df['Season'] = np.where(df['DateT'] == )