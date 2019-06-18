# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 05:18:54 2019

@author: egwil
"""
#Export results for further analysis

import xlsxwriter
workbook = xlsxwriter.Workbook('C:/Users/egwil/OneDrive - University of Cape Town/UCT/Research/Data/data/Analysis.xlsx')

worksheet_xdatapoints = workbook.add_worksheet(X_train)
worksheet_xdatavalues = workbook.add_worksheet(y_train)
worksheet_ydatapoints = workbook.add_worksheet(X_test)
worksheet_ydatavalues = workbook.add_worksheet(y_test)