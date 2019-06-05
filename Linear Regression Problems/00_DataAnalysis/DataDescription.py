# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:09:36 2019

@author: egwil
"""

#Data exploration

"""
Step 1: Import libraries
"""

#import matplotlib for visualisations
from dateutil.parser import parse #use parser make the date colum to be parsed as a date field
import matplotlib as mpl
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
import numpy as np

"""
Step 2: Set variables 
"""
filepath = 'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/rainfall and temperature.xlsx'

#filepath = 'C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/Stations.xls'
sheetname = 'Rainfall and Temperature '
feature = 'MaxTemp (°C)'

"""
Step 3: Import as Dataframe
"""

df = pd.read_excel(filepath, sheet_name=sheetname )

"""
Step 4: view data overview 
"""

#look at first 20 rows of data 
print(df.describe)

