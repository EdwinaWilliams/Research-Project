# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:15:44 2019

@author: egwil
"""

#Import libraries
import datetime 
import pandas as pd  

#empty dataframe to store values 
combine = pd.DataFrame(columns=['Current Date' ,'Current MaxTemp' , 'Y1 Prev Date', 'Y1 Prev Temp' ,'Y2 Prev Date', 'Y2 Prev Temp' ,'Y3 Prev Date', 'Y3 Prev Temp','Y4 Prev Date', 'Y4 Prev Temp' ,'Y5 Prev Date', 'Y5 Prev Temp'])

#Importing data 
filepath = ('C:/Users/egwil/OneDrive/Desktop/Results/01_Missing Values Replaced.xlsx')

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



for i in index:
    k =i+1
    #current variables 
    df_current_dt = df.iloc[i:k, 0:1]
    d0 = df_current_dt.iloc[0].values
    df_current_tmp = df.iloc[i:k, 6:7] 
    t0 = df_current_tmp.values#.reshape(-1, 1)
    #print(kkkll)
    #***********************************************************************************
    #First Year Prior
    #***********************************************************************************
    #Getting values 
    date1 = df.iloc[i:k, 10:11]
    d1 = date1.iloc[0].values
    year1 = date1['Year1'].map(lambda x: x.year)
    #y1= year1.item()
    month1 = date1['Year1'].map(lambda x: x.month)
    #m1 = month1.item()
    day1 = date1['Year1'].map(lambda x: x.day)
    #d1 = day1.item()
    
    df_values1 = df_new[(df_new['DateT'] == datetime.date(year1,month1,day1))]##datetime.date(date1))] #df.loc[datetime.date(year)]
    df_prev1_tmp = df_values1['MaxTemp (°C)']
    t1 = df_prev1_tmp.values
    #t1 = df_prev1_tmp.item()
    
    #***********************************************************************************
    #Second Year Prior
    #***********************************************************************************
    #Getting values 
    date2 = df.iloc[i:k, 11:12]
    d2 = date2.iloc[0].values
    year2 = date2['Year2'].map(lambda x: x.year)
    month2 = date2['Year2'].map(lambda x: x.month)
    day2 = date2['Year2'].map(lambda x: x.day)

    df_values2 = df_new[(df_new['DateT'] == datetime.date(year2,month2,day2))]##datetime.date(date1))] #df.loc[datetime.date(year)]
    df_prev2_tmp = df_values2['MaxTemp (°C)']
    t2 = df_prev2_tmp.values
    
    #***********************************************************************************
    #Third Year Prior
    #***********************************************************************************
    #Getting values 
    date3 = df.iloc[i:k, 12:13]
    d3= date3.iloc[0].values
    year3 = date3['Year3'].map(lambda x: x.year)
    month3 = date3['Year3'].map(lambda x: x.month)
    day3 = date3['Year3'].map(lambda x: x.day)

    df_values3 = df_new[(df_new['DateT'] == datetime.date(year3,month3,day3))]##datetime.date(date1))] #df.loc[datetime.date(year)]
    df_prev3_tmp = df_values3['MaxTemp (°C)']
    t3 = df_prev3_tmp.values
    
    #***********************************************************************************
    #Fourth Year Prior
    #***********************************************************************************
    #Getting values 
    date4 = df.iloc[i:k, 13:14]
    d4 = date4.iloc[0].values
    year4 = date4['Year4'].map(lambda x: x.year)
    month4 = date4['Year4'].map(lambda x: x.month)
    day4 = date4['Year4'].map(lambda x: x.day)

    df_values4 = df_new[(df_new['DateT'] == datetime.date(year4,month4,day4))]##datetime.date(date1))] #df.loc[datetime.date(year)]
    df_prev4_tmp = df_values4['MaxTemp (°C)']
    t4 = df_prev4_tmp.values
    
    #***********************************************************************************
    #Fifth Year Prior
    #***********************************************************************************
    #Getting values 
    date5 = df.iloc[i:k, 14:15]
    d5 = date5.iloc[0].values
    year5 = date5['Year5'].map(lambda x: x.year)
    month5 = date5['Year5'].map(lambda x: x.month)
    day5 = date5['Year5'].map(lambda x: x.day)

    df_values5 = df_new[(df_new['DateT'] == datetime.date(year5,month5,day5))]##datetime.date(date1))] #df.loc[datetime.date(year)]
    df_prev5_tmp = df_values5['MaxTemp (°C)']
    t5 = df_prev5_tmp.values



    #Combine for export values 
    gather = pd.DataFrame({'Current Date' :[d0],'Current MaxTemp' : [t0], 'Y1 Prev Date': [d1], 'Y1 Prev Temp': [t1]   , 'Y2 Prev Date': [d2], 'Y2 Prev Temp': [t2] , 'Y3 Prev Date': [d3], 'Y3 Prev Temp': [t3], 'Y4 Prev Date': [d4], 'Y4 Prev Temp': [t4] , 'Y5 Prev Date': [d5], 'Y5 Prev Temp': [t5] }) 
    combine = combine.append(gather)

combine.to_excel(r'C:\Users\egwil\OneDrive\Desktop\tmpDir\5_year_Avg_PMB.xlsx')
   