# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:19:05 2019

@author: egwil
"""
import pandas as pd
#start = 0
#stop = 2
#wind_num = 1 
#
#list = [1, 2, 3, 4, 5]
#
#for i in list:
#    while stop != 11 :
#        wind_nam = 'w' + str(wind_num)
#        (print(wind_nam.index)
#        start += 1 
#        stop += 1
#        wind_num += 1 
#        
        
df_windows = pd.DataFrame({'Window Number':0 , 'Window Values':0 })
df_windows.to_excel(r'C:\Users\egwil\OneDrive\Desktop\Results\SVM Window Test Info.xlsx')
