# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:15:44 2019

@author: egwil
"""

#Import libraries
import datetime 
import pandas as pd  

#empty dataframe to store values 

combine = pd.DataFrame(columns=['Current Date' ,'Current MaxTemp' , 'Y1 Prev Date', 'y1 Prev Temp'])

#Importing data 
filepath = (r'C:\Users\egwil\OneDrive\Desktop\Results\01_Missing Values Replaced.xlsx')

#Import data 
df = pd.read_excel(filepath)  

df['Year1'] =  df['DateT'].apply(lambda x: x - pd.DateOffset(years=1))
df['Year2'] =  df['DateT'].apply(lambda x: x - pd.DateOffset(years=2))
df['Year3'] =  df['DateT'].apply(lambda x: x - pd.DateOffset(years=3))
df['Year4'] =  df['DateT'].apply(lambda x: x - pd.DateOffset(years=4))
df['Year5'] =  df['DateT'].apply(lambda x: x - pd.DateOffset(years=5))
#'MaxTemp (°C)'
df_new = temps = df.loc[:,:].copy() # df['DateT'] >= '2007-01-01'

index =  df[:].index.values.tolist() #reshape(-1, 1)

df_pred_vals = pd.DataFrame(columns = ['Index', 'Test Value/s', 'Predict Value/s'])


for i in index:
    k =i+1
    date1 = df.iloc[i:k, 7:8]
    year = date1['Year1'].map(lambda x: x.year)
    #print(year)
    month = date1['Year1'].map(lambda x: x.month)
    #print(month)
    day = date1['Year1'].map(lambda x: x.day)
    #print(day)
        
   # print(df.iloc[i:k, 0:1])
    #print(date1)
    df_current_dt = df.iloc[i:k, 0:1]
    df_current_tmp = df.iloc[i:k, 4:5]  
    
    df_values = df_new[(df_new['DateT'] == datetime.date(year,month,day))]##datetime.date(date1))] #df.loc[datetime.date(year)]
    
    df_prev1_tmp = df_values['MaxTemp (°C)']
    
    gather = pd.DataFrame({'Current Date' :[df_current_dt],'Current MaxTemp' : [df_current_tmp], 'Y1 Prev Date': [date1], 'y1 Prev Temp': [df_prev1_tmp]}) 

    combine = combine.append(gather)
    
    #df.query(date1 == df['DateT'])
    #print(df_values)#[where date is equal to date 
    #    datet = df['DateT'].apply(lambda x: x + pd.Timedelta(days=1))

   # datet = df['DateT'].apply(lambda x: x + pd.Timedelta(days=1))
   # print(datet)
    #print(df.loc[date1: ])
    
#    q = 1
#    while q != 2:
#        pink = df['DateT'] == date1
#        l = df[pink]
#        print(l)
#        q += 1
    #if :
        #print(df['DateT'])
    #df_f  = df[filt]
    
#    if : 
#        temp1 = df['MaxTemp (°C)']
#    print(temp1)
    
#    df_slice = df.index(i).values
#    print(df_slice)
#for index, row in df.iterrows():
#    if row['DateT'] == row['Year1']:
#        temp1 = row['MaxTemp (°C)']
#    elif row['DateT'] == row['Year2']:
#        temp2 = row['MaxTemp (°C)']
#    elif row['DateT'] == row['Year3']:
#        temp3 = row['MaxTemp (°C)']
#    elif row['DateT'] == row['Year4']:
#        temp4 = row['MaxTemp (°C)']
#    elif row['DateT'] == row['Year5']:
#        temp5 = row['MaxTemp (°C)']    
##    temp= df_filtered[ 4:5]
#    pink = (temp1+temp2+temp3+temp4+temp5)
#    print(pink)