import pandas as pd
from PyQt6 import QtWidgets
from backend.readfile import read
def load_data_to_table(tableWidget,df, filter_column=None, filter_na=False,search_text=None):
    
   
    
    if filter_column is not None:
        if filter_na:
            df = df[df.iloc[:, filter_column].notna()]  
        else:
            df = df[df.iloc[:, filter_column].isna()] 
    
    if search_text:  
        
        df = df[df.iloc[:, 0].str.lower().str.startswith(search_text, na=False)]
        
   
    
    tableWidget.setRowCount(0)  
    tableWidget.setRowCount(len(df)) 
    tableWidget.setColumnCount(df.shape[1])  
    tableWidget.setColumnWidth(0, 205)  # 1. sütun genişliği 150 px
    tableWidget.setColumnWidth(1, 205)  # 2. sütun genişliği 200 px
    tableWidget.setColumnWidth(2, 205)  # 3. sütun genişliği 250 px
    
    for row in range(df.shape[0]):  
        for col in range(df.shape[1]):
            print(df.iloc[row, col])
            if col!=0:
                element=str(df.iloc[row, col]).split(" ")[0]
            else:
                element=str(df.iloc[row, col])
            item = QtWidgets.QTableWidgetItem(element)
          
            tableWidget.setItem(row, col, item)