# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:54:48 2024

@author: Admin
"""
# Pre-processing:
    
# Importing the pandas library and aliasing it as pd
import pandas as pd
# Reading the CSV file into a pandas DataFrame
medical_dataset=pd.read_csv("Medical Inventory Optimaization Dataset.csv")
# Generating descriptive statistics of the dataset
medical_dataset.describe()
# Outputting the column names of the dataset
medical_dataset.columns
# Outputting the data types of each column in the dataset
medical_dataset.dtypes


# typecasting:
# In medical_dataset, "dateofbill" is not in the correct format, so we are converting 
# it to a date datatype.
# Importing the datetime module from the datetime library
  
# Replacing '-' with '/' in the 'Dateofbill' column
medical_dataset['Dateofbill'] = medical_dataset['Dateofbill'].str.replace(r'-', '/', regex=True)

# Converting 'Dateofbill' column to datetime format with specified format
medical_dataset['Dateofbill'] = pd.to_datetime(medical_dataset['Dateofbill'], format='%m/%d/%Y')

# Extracting only the date part from the 'Dateofbill' column
medical_dataset['Dateofbill'] = medical_dataset['Dateofbill'].dt.date
print(medical_dataset['Dateofbill'])

# Convert 'Dateofbill' column to datetime format
medical_dataset['Dateofbill'] = pd.to_datetime(medical_dataset['Dateofbill'])


# ------------------------------------------------------------------------------
# duplication handling:
# before droping duplicate rows
medical_dataset.shape
# output:
#     (14218, 14)

# calculates the total number of duplicate rows
medical_dataset.duplicated().sum()
# output:
#     26

medical_dataset_duplicates=medical_dataset.duplicated()
print(medical_dataset_duplicates)

medical_dataset=medical_dataset.drop_duplicates()
print(medical_dataset)

# after droping duplicate rows
medical_dataset.shape  
# output:
    # (14192, 14)


# ---------------------------------------------------------------------------




total_missing_value=medical_dataset.isnull().sum()
print(total_missing_value)
# output:
# Typeofsales          0
# Patient_ID           0
# Specialisation       0
# Dept                 0
# Dateofbill           0
# Quantity             0
# ReturnQuantity       0
# Final_Cost           0
# Final_Sales          0
# RtnMRP               0
# Formulation        650
# DrugName          1659
# SubCat            1659
# SubCat1           1682
# dtype: int64


percentage_missing_value=medical_dataset.isnull().mean()*100
print(percentage_missing_value)
# output:
# Typeofsales        0.000000
# Patient_ID         0.000000
# Specialisation     0.000000
# Dept               0.000000
# Dateofbill         0.000000
# Quantity           0.000000
# ReturnQuantity     0.000000
# Final_Cost         0.000000
# Final_Sales        0.000000
# RtnMRP             0.000000
# Formulation        4.580045
# DrugName          11.689684
# SubCat            11.689684
# SubCat1           11.851747
# dtype: float64

medical_dataset.columns

# if the dataset is mcar then the distribution of the variable of the reduced dataset:
# should matches the distribution in the original dataset

col = [var for var in medical_dataset.columns if medical_dataset[var].isnull().mean() <0.05 and medical_dataset[var].isnull().mean() > 0]
col
medical_dataset[col]

len(medical_dataset[col].dropna())/len(medical_dataset)

new_medical_dataset=medical_dataset[col].dropna()
new_medical_dataset

medical_dataset.shape,new_medical_dataset.shape


medical_dataset