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
    df_current_tmp = df.iloc[i:k, 4:5]  
    
    #***********************************************************************************
    #First Year Prior
    #***********************************************************************************
    #Getting values 
    date1 = df.iloc[i:k, 7:8]
    year1 = date1['Year1'].map(lambda x: x.year)
    month1 = date1['Year1'].map(lambda x: x.month)
    day1 = date1['Year1'].map(lambda x: x.day)

    df_values1 = df_new[(df_new['DateT'] == datetime.date(year1,month1,day1))]##datetime.date(date1))] #df.loc[datetime.date(year)]
    df_prev1_tmp = df_values1['MaxTemp (°C)']
    
    #***********************************************************************************
    #Second Year Prior
    #***********************************************************************************
    #Getting values 
    date2 = df.iloc[i:k, 8:9]
    year2 = date2['Year2'].map(lambda x: x.year)
    month2 = date2['Year2'].map(lambda x: x.month)
    day2 = date2['Year2'].map(lambda x: x.day)

    df_values2 = df_new[(df_new['DateT'] == datetime.date(year2,month2,day2))]##datetime.date(date1))] #df.loc[datetime.date(year)]
    df_prev2_tmp = df_values2['MaxTemp (°C)']

    #***********************************************************************************
    #Third Year Prior
    #***********************************************************************************
    #Getting values 
    date3 = df.iloc[i:k, 9:10]
    year3 = date3['Year3'].map(lambda x: x.year)
    month3 = date3['Year3'].map(lambda x: x.month)
    day3 = date3['Year3'].map(lambda x: x.day)

    df_values3 = df_new[(df_new['DateT'] == datetime.date(year3,month3,day3))]##datetime.date(date1))] #df.loc[datetime.date(year)]
    df_prev3_tmp = df_values3['MaxTemp (°C)']

    #***********************************************************************************
    #Fourth Year Prior
    #***********************************************************************************
    #Getting values 
    date4 = df.iloc[i:k, 10:11]
    year4 = date4['Year4'].map(lambda x: x.year)
    month4 = date4['Year4'].map(lambda x: x.month)
    day4 = date4['Year4'].map(lambda x: x.day)

    df_values4 = df_new[(df_new['DateT'] == datetime.date(year4,month4,day4))]##datetime.date(date1))] #df.loc[datetime.date(year)]
    df_prev4_tmp = df_values4['MaxTemp (°C)']

    #***********************************************************************************
    #Fifth Year Prior
    #***********************************************************************************
    #Getting values 
    date5 = df.iloc[i:k, 11:12]
    year5 = date5['Year5'].map(lambda x: x.year)
    month5 = date5['Year5'].map(lambda x: x.month)
    day5 = date5['Year5'].map(lambda x: x.day)

    df_values5 = df_new[(df_new['DateT'] == datetime.date(year5,month5,day5))]##datetime.date(date1))] #df.loc[datetime.date(year)]
    df_prev5_tmp = df_values5['MaxTemp (°C)']




    #Combine for export values 
    gather = pd.DataFrame({'Current Date' :[df_current_dt],'Current MaxTemp' : [df_current_tmp], 'Y1 Prev Date': [date1], 'Y1 Prev Temp': [df_prev1_tmp]   , 'Y2 Prev Date': [date2], 'Y2 Prev Temp': [df_prev2_tmp] , 'Y3 Prev Date': [date3], 'Y3 Prev Temp': [df_prev3_tmp], 'Y4 Prev Date': [date4], 'Y4 Prev Temp': [df_prev4_tmp] , 'Y5 Prev Date': [date5], 'Y5 Prev Temp': [df_prev5_tmp] }) 
    combine = combine.append(gather)

combine.to_excel(r'C:\Users\egwil\OneDrive\Desktop\tmpDir\5_year_Avg_Pretoria.xlsx')
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