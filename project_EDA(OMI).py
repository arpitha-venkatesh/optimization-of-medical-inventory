# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 10:43:39 2024

@author: Admin
"""
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


# Importing the datetime module from the datetime library
from datetime import datetime  
# Replacing '-' with '/' in the 'Dateofbill' column
medical_dataset['Dateofbill'] = medical_dataset['Dateofbill'].str.replace(r'-', '/', regex=True)

# Converting 'Dateofbill' column to datetime format with specified format
medical_dataset['Dateofbill'] = pd.to_datetime(medical_dataset['Dateofbill'], format='%m/%d/%Y')

# Extracting only the date part from the 'Dateofbill' column
medical_dataset['Dateofbill'] = medical_dataset['Dateofbill'].dt.date
print(medical_dataset['Dateofbill'])

# Convert 'Dateofbill' column to datetime format
medical_dataset['Dateofbill'] = pd.to_datetime(medical_dataset['Dateofbill'])

# Extract month from the 'Dateofbill' column
medical_dataset['month'] = medical_dataset['Dateofbill'].dt.month

# Extract week number from the 'Dateofbill' column
medical_dataset['week'] = medical_dataset['Dateofbill'].dt.isocalendar().week


#  EDA(EXPLORATORY DATA ANALYSIS):
#  1ST MOMENT BUSINESS DECISION:
#  MEAN:
mean_quantity = medical_dataset['Quantity'].mean()
mean_return_quantity = medical_dataset['ReturnQuantity'].mean()
mean_final_cost = medical_dataset['Final_Cost'].mean()
mean_final_sales = medical_dataset['Final_Sales'].mean()
mean_rtn_mrp = medical_dataset['RtnMRP'].mean()

# Print out the results
print("Mean Quantity:", mean_quantity)
print("Mean Return Quantity:", mean_return_quantity)
print("Mean Final Cost:", mean_final_cost)
print("Mean Final Sales:", mean_final_sales)
print("Mean RtnMRP:", mean_rtn_mrp)
# output:
#     Mean Quantity: 2.2317484878323253
#     Mean Return Quantity: 0.2919538613025742
#     Mean Final Cost: 124.82395695597131
#     Mean Final Sales: 234.0383004642003
#     Mean RtnMRP: 29.126754958503305
    
# MEDIAN:
median_quantity = medical_dataset['Quantity'].median()
median_return_quantity = medical_dataset['ReturnQuantity'].median()
median_final_cost = medical_dataset['Final_Cost'].median()
median_final_sales = medical_dataset['Final_Sales'].median()
median_rtn_mrp = medical_dataset['RtnMRP'].median()

# Print out the results
print("Median Quantity:", median_quantity)
print("Median Return Quantity:", median_return_quantity)
print("Median Final Cost:", median_final_cost)
print("Median Final Sales:", median_final_sales)
print("Median RtnMRP:", median_rtn_mrp)
# output:
#     Median Quantity: 1.0
#     Median Return Quantity: 0.0
#     Median Final Cost: 53.65
#     Median Final Sales: 86.424
#     Median RtnMRP: 0.0

# MODE:
mode_typeofsales = medical_dataset['Typeofsales'].mode()
mode_specialisation = medical_dataset['Specialisation'].mode()
mode_dept = medical_dataset['Dept'].mode()
mode_formulation = medical_dataset['Formulation'].mode()
mode_drugname = medical_dataset['DrugName'].mode()
mode_subcat = medical_dataset['SubCat'].mode()
mode_subcat1 = medical_dataset['SubCat1'].mode()

# Print out the results
print("Mode Type of Sales:", mode_typeofsales)
print("Mode Specialisation:", mode_specialisation)
print("Mode Department:", mode_dept)
print("Mode Formulation:", mode_formulation)
print("Mode Drug Name:", mode_drugname)
print("Mode Subcategory:", mode_subcat)
print("Mode Subcategory 1:", mode_subcat1)
# output:
#     Mode Type of Sales: 0    Sale
    
#     Mode Specialisation: 0    Specialisation4
   
#     Mode Department: 0    Department1
   
#     Mode Formulation: 0    Form1
    
#     Mode Drug Name: 0    SODIUM CHLORIDE IVF 100ML
   
#     Mode Subcategory: 0    INJECTIONS
    
#     Mode Subcategory 1: 0    INTRAVENOUS & OTHER STERILE SOLUTIONS
   

# second moment of bussiness understanding(measure of dispersion):
# variance:
variance_quantity = medical_dataset['Quantity'].var()
variance_return_quantity = medical_dataset['ReturnQuantity'].var()
variance_final_cost = medical_dataset['Final_Cost'].var()
variance_final_sales = medical_dataset['Final_Sales'].var()
variance_rtn_mrp = medical_dataset['RtnMRP'].var()

# Print out the results
print("Variance Quantity:", variance_quantity)
print("Variance Return Quantity:", variance_return_quantity)
print("Variance Final Cost:", variance_final_cost)
print("Variance Final Sales:", variance_final_sales)
print("Variance RtnMRP:", variance_rtn_mrp)
# output:
#     Variance Quantity: 26.337862329088537
#     Variance Return Quantity: 2.7005064023169365
#     Variance Final Cost: 216023.04539371582
#     Variance Final Sales: 450592.0976656481
#     Variance RtnMRP: 33219.558938268776

# standared deviation
std_dev_quantity = medical_dataset['Quantity'].std()
std_dev_return_quantity = medical_dataset['ReturnQuantity'].std()
std_dev_final_cost = medical_dataset['Final_Cost'].std()
std_dev_final_sales = medical_dataset['Final_Sales'].std()
std_dev_rtn_mrp = medical_dataset['RtnMRP'].std()

# Print out the results
print("Standard Deviation Quantity:", std_dev_quantity)
print("Standard Deviation Return Quantity:", std_dev_return_quantity)
print("Standard Deviation Final Cost:", std_dev_final_cost)
print("Standard Deviation Final Sales:", std_dev_final_sales)
print("Standard Deviation RtnMRP:", std_dev_rtn_mrp)
# output:
# Standard Deviation Quantity: 5.13204270530639
# Standard Deviation Return Quantity: 1.6433217586087445
# Standard Deviation Final Cost: 464.7827937797567
# Standard Deviation Final Sales: 671.2615717182447
# Standard Deviation RtnMRP: 182.26233548999852

# range:
range_quantity = max(medical_dataset['Quantity']) - min(medical_dataset['Quantity'])
range_return_quantity = max(medical_dataset['ReturnQuantity']) - min(medical_dataset['ReturnQuantity'])
range_final_cost = max(medical_dataset['Final_Cost']) - min(medical_dataset['Final_Cost'])
range_final_sales = max(medical_dataset['Final_Sales']) - min(medical_dataset['Final_Sales'])
range_rtn_mrp = max(medical_dataset['RtnMRP']) - min(medical_dataset['RtnMRP'])

# Print out the results
print("Range Quantity:", range_quantity)
print("Range Return Quantity:", range_return_quantity)
print("Range Final Cost:", range_final_cost)
print("Range Final Sales:", range_final_sales)
print("Range RtnMRP:", range_rtn_mrp)
# output:
#     Range Quantity: 150
#     Range Return Quantity: 50
#     Range Final Cost: 33138.0
#     Range Final Sales: 39490.0
#     Range RtnMRP: 8014.0


# third moment of bussiness understanding:
# skewness:
skewness_quantity = medical_dataset['Quantity'].skew()
skewness_return_quantity = medical_dataset['ReturnQuantity'].skew()
skewness_final_cost = medical_dataset['Final_Cost'].skew()
skewness_final_sales = medical_dataset['Final_Sales'].skew()
skewness_rtn_mrp = medical_dataset['RtnMRP'].skew()

# Print out the results
print("Skewness Quantity:", skewness_quantity)
print("Skewness Return Quantity:", skewness_return_quantity)
print("Skewness Final Cost:", skewness_final_cost)
print("Skewness Final Sales:", skewness_final_sales)
print("Skewness RtnMRP:", skewness_rtn_mrp) 
# output:
#     Skewness Quantity: 11.34103427676747
#     Skewness Return Quantity: 17.172364771343634
#     Skewness Final Cost: 34.508214502400946
#     Skewness Final Sales: 21.006721582359116
#     Skewness RtnMRP: 15.797853037440984
    
    
# forth moment of bussiness understanding
# kurtosis:
kurtosis_quantity = medical_dataset['Quantity'].kurt()
kurtosis_return_quantity = medical_dataset['ReturnQuantity'].kurt()
kurtosis_final_cost = medical_dataset['Final_Cost'].kurt()
kurtosis_final_sales = medical_dataset['Final_Sales'].kurt()
kurtosis_rtn_mrp = medical_dataset['RtnMRP'].kurt()

# Print out the results
print("Kurtosis Quantity:", kurtosis_quantity)
print("Kurtosis Return Quantity:", kurtosis_return_quantity)
print("Kurtosis Final Cost:", kurtosis_final_cost)
print("Kurtosis Final Sales:", kurtosis_final_sales)
print("Kurtosis RtnMRP:", kurtosis_rtn_mrp)
# output:
#     Kurtosis Quantity: 180.15385837022285
#     Kurtosis Return Quantity: 409.41691374471526
#     Kurtosis Final Cost: 2025.8664752637628
#     Kurtosis Final Sales: 948.5227111226725
#     Kurtosis RtnMRP: 403.52494081462515

# graphical representation:
# univarient:
# boxplot
import seaborn as sns
import matplotlib.pyplot as plt
# Create subplots with boxplots for each variable
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
sns.boxplot(y=medical_dataset['Quantity'], color='skyblue')
plt.title('Boxplot of Quantity')

plt.subplot(2, 3, 2)
sns.boxplot(y=medical_dataset['ReturnQuantity'], color='salmon')
plt.title('Boxplot of ReturnQuantity')

plt.subplot(2, 3, 3)
sns.boxplot(y=medical_dataset['Final_Cost'], color='green')
plt.title('Boxplot of Final_Cost')

plt.subplot(2, 3, 4)
sns.boxplot(y=medical_dataset['Final_Sales'], color='orange')
plt.title('Boxplot of Final_Sales')

plt.subplot(2, 3, 5)
sns.boxplot(y=medical_dataset['RtnMRP'], color='purple')
plt.title('Boxplot of RtnMRP')

plt.tight_layout()
plt.show()

# histogram
plt.figure(figsize=(15,10))
plt.subplot(2,3,1)
plt.hist(medical_dataset['Typeofsales'], color='green', edgecolor='black')
plt.xlabel('Typeofsales')
plt.ylabel('Frequency')
plt.title('Histogram of Typeofsales')


plt.subplot(2,3,2)
plt.hist(medical_dataset['Patient_ID'], color='green', edgecolor='black')
plt.xlabel('Patient_ID')
plt.ylabel('Frequency')
plt.title('Histogram of Patient_ID')


plt.subplot(2,3,3)
plt.hist(medical_dataset['Specialisation'], color='green', edgecolor='black')
plt.xlabel('Specialisation')
plt.ylabel('Frequency')
plt.title('Histogram of Specialisation')


plt.subplot(2,3,4)
plt.hist(medical_dataset['Dept'], color='green', edgecolor='black')
plt.xlabel('Dept')
plt.ylabel('Frequency')
plt.title('Histogram of Dept')
plt.show()

plt.figure(figsize=(15,10))
plt.subplot(2,3,1)
plt.hist(medical_dataset['Quantity'], color='green', edgecolor='black')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.title('Histogram of Quantity')

plt.subplot(2,3,2)
plt.hist(medical_dataset['ReturnQuantity'], color='green', edgecolor='black')
plt.xlabel('ReturnQuantity')
plt.ylabel('Frequency')
plt.title('Histogram of ReturnQuantity')


plt.subplot(2,3,3)
plt.hist(medical_dataset['Final_Cost'], color='green', edgecolor='black')
plt.xlabel('Final_Cost')
plt.ylabel('Frequency')
plt.title('Histogram of Final_Cost')


plt.subplot(2,3,4)
plt.hist(medical_dataset['Final_Sales'], color='green', edgecolor='black')
plt.xlabel('Final_Sales')
plt.ylabel('Frequency')
plt.title('Histogram of Final_Sales')


plt.subplot(2,3,5)
plt.hist(medical_dataset['RtnMRP'], color='green', edgecolor='black')
plt.xlabel('RtnMRP')
plt.ylabel('Frequency')
plt.title('Histogram of RtnMRP')
plt.show()


# plt.figure(figsize=(15,10))
# plt.subplot(2,3,1)
# plt.hist(medical_dataset['Formulation'], color='green', edgecolor='black')
# plt.xlabel('Formulation')
# plt.ylabel('Frequency')
# plt.title('Histogram of Formulation')


# plt.subplot(2,3,2)
# plt.hist(medical_dataset['DrugName'], color='green', edgecolor='black')
# plt.xlabel('DrugName')
# plt.ylabel('Frequency')
# plt.title('Histogram of DrugName ')


# plt.subplot(2,3,3)
# plt.hist(medical_dataset['SubCat'], color='green', edgecolor='black')
# plt.xlabel('SubCat')
# plt.ylabel('Frequency')
# plt.title('Histogram of SubCat ')


# plt.subplot(2,3,4)
# plt.hist(medical_dataset['SubCat1'], color='green', edgecolor='black')
# plt.xlabel('SubCat1')
# plt.ylabel('Frequency')
# plt.title('Histogram of SubCat1 ')
# plt.show()

# Due to missing values in the formulation,drug_name ,subcat,subcat1 columns
# the histograms for 'drug_name', 'subcat', and 'subcat1' columns are displaying errors.

# scatter plot

plt.figure(figsize=(15, 10))

# Scatter plot of Quantity vs ReturnQuantity
plt.subplot(2,3,1)
plt.scatter(x=medical_dataset['Quantity'], y=medical_dataset['ReturnQuantity'],color="green")
plt.title("Scatter plot of Quantity vs ReturnQuantity")
plt.xlabel("Quantity")
plt.ylabel("ReturnQuantity")

# Scatter plot of Quantity vs Final_Cost
plt.subplot(2,3,2)
plt.scatter(x=medical_dataset['Quantity'], y=medical_dataset['Final_Cost'],color="green")
plt.title("Scatter plot of Quantity vs Final_Cost")
plt.xlabel("Quantity")
plt.ylabel("Final_Cost")


# Scatter plot of Quantity vs Final_Sales
plt.subplot(2,3,3)
plt.scatter(x=medical_dataset['Quantity'], y=medical_dataset['Final_Sales'],color="green")
plt.title("Scatter plot of Quantity vs Final_Sales")
plt.xlabel("Quantity")
plt.ylabel("Final_Sales")

# Scatter plot of Final_Cost vs Final_Sales
plt.subplot(2,3,4)
plt.scatter(x=medical_dataset['Final_Cost'], y=medical_dataset['Final_Sales'],color="green")
plt.title("Scatter plot of Final_Cost vs Final_Sales ")
plt.xlabel("Final_Cost")
plt.ylabel("Final_Sales")
plt.show()




# quantities sold per month:
quantity_sold_per_month=medical_dataset.groupby('month')['Quantity'].sum()
quantity_sold_per_month=quantity_sold_per_month.sort_values(ascending=False)
print(quantity_sold_per_month)
# output:
    # month
    # 12    3105
    # 7     3010
    # 8     2983
    # 4     2948
    # 3     2815
    # 5     2647
    # 11    2631
    # 10    2571
    # 9     2462
    # 1     2310
    # 6     2126
    # 2     2123
    # Name: Quantity, dtype: int64
    
# The output shows the quantities sold per month, sorted in descending order based on the quantity sold.
# It appears that December has the highest quantity sold, followed closely by July.
# Conversely, January and June seem to have the lowest quantities sold.
# There seems to be some seasonal variation in the quantities sold throughout the year.
# For instance, the quantity sold appears to be lower in the early months of the year (January, February),
# increases in the middle months (March to July), dips slightly in August and September,
# and then rises again towards the end of the year (October to December).



# total quantity of returned items for each month
quantity_return_per_month=medical_dataset.groupby('month')['ReturnQuantity'].sum()
quantity_return_per_month=quantity_return_per_month.sort_values(ascending=False)
print(quantity_return_per_month)
# output:
#     month
#     8     558
#     5     470
#     11    384
#     12    366
#     3     343
#     4     329
#     7     310
#     1     294
#     6     291
#     2     290
#     9     272
#     10    244
#     Name: ReturnQuantity, dtype: int64

# The data shows the total quantity of returned items for each month, sorted in descending order:
# August had the highest quantity of returned items with 558 units.
# May had the second-highest quantity of returns, totaling 470 units.
# November and December followed with 384 and 366 units returned, respectively.
# The trend continues with March, April, and July, each having over 300 units returned.
# January had 294 units returned, and June had 291 units returned.
# February, September, and October had lower return quantities, ranging from 244 to 290 units.


# total quantity of returned items for each week
quantity_return_per_week=medical_dataset.groupby('week')['ReturnQuantity'].sum()
quantity_return_per_week=quantity_return_per_week.sort_values(ascending=False)
print(quantity_return_per_week)


# Calculate the total final sales per month :
Final_Sales_per_month=medical_dataset.groupby('month')['Final_Sales'].sum()
Final_Sales_per_month=Final_Sales_per_month.sort_values(ascending=False)
print(Final_Sales_per_month)
# output:
#     month
#     12    412259.126
#     8     319996.630
#     7     309785.630
#     5     300612.102
#     11    273303.022
#     4     267918.874
#     10    258533.458
#     3     250913.852
#     2     247230.908
#     1     236331.070
#     9     234034.332
#     6     216637.552
#     Name: Final_Sales, dtype: float64
# December (Month 12) had the highest total final sales, totaling approximately $412,259.13.
# Following December, August (Month 8) and July (Month 7) had the next highest total final sales,
# with approximately $319,996.63 and $309,785.63 respectively.
# There's a noticeable decrease in total final sales from August to June, with June having the 
# lowest total final sales among the listed months, at approximately $216,637.55.

Final_Sales_per_week=medical_dataset.groupby('week')['Final_Sales'].sum()
Final_Sales_per_week=Final_Sales_per_week.sort_values(ascending=False)
print(Final_Sales_per_week)


total_quantity_sold_per_drug=medical_dataset.groupby('DrugName')['Quantity'].sum()
total_quantity_sold_per_drug=total_quantity_sold_per_drug.sort_values(ascending=False)
print(total_quantity_sold_per_drug)
# output:
#     DrugName
#     SODIUM CHLORIDE IVF 100ML              1278
#     SEVOFLURANE 99.97%                     1193
#     SODIUM CHLORIDE 0.9%                    948
#     ONDANSETRON 2MG/ML                      933
#     MULTIPLE ELECTROLYTES 500ML IVF         919

#     MYCOPHENOLATE MOFETIL 250MG/ML SUSP       0
#     TORASEMIDE 20MG                           0
#     TORASEMIDE 40MG TAB                       0
#     MULTI VITAMINS 15ML DROPS                 0
#     MEROPENEM 250MG INJ                       0
#     Name: Quantity, Length: 751, dtype: int64

total_quantity_sold_per_month_drug=medical_dataset.groupby(['month','DrugName'])['Quantity'].sum()
total_quantity_sold_per_month_drug=total_quantity_sold_per_month_drug.sort_values(ascending=False)
print(total_quantity_sold_per_month_drug)
# output:
#     month  DrugName                                   
#     3      SEVOFLURANE 99.97%                             258
#     1      SEVOFLURANE 99.97%                             230
#     4      SODIUM CHLORIDE IVF 100ML                      198
#     11     WATER FOR INJECTION 10ML SOLUTION              185
#     6      SODIUM CHLORIDE IVF 100ML                      183

#     3      PRUCALOPRIDE 1MG                                 0
#     8      IBANDRONIC ACID 150MG TAB                        0
#     1      NUTRITION FOR HEPATIC PATIENTS 400GM POWDER      0
#     12     LEVETIRACETAM 1GM TAB                            0
#     1      MULTI VITAMINS 15ML DROPS                        0
#     Name: Quantity, Length: 3081, dtype: int64

total_quantity_sold_per_drug_subcat_subcat1=medical_dataset.groupby(['DrugName','SubCat','SubCat1'])['Quantity'].sum()
total_quantity_sold_per_drug_subcat_subcat1 =total_quantity_sold_per_drug_subcat_subcat1.sort_values(ascending=False)
print(total_quantity_sold_per_drug_subcat_subcat1 )
# output:
#     DrugName                             SubCat                        SubCat1                                
#     SODIUM CHLORIDE IVF 100ML            IV FLUIDS, ELECTROLYTES, TPN  INTRAVENOUS & OTHER STERILE SOLUTIONS      1278
#     SEVOFLURANE 99.97%                   LIQUIDS & SOLUTIONS           ANAESTHETICS                               1193
#     SODIUM CHLORIDE 0.9%                 IV FLUIDS, ELECTROLYTES, TPN  INTRAVENOUS & OTHER STERILE SOLUTIONS       948
#     ONDANSETRON 2MG/ML                   INJECTIONS                    GASTROINTESTINAL & HEPATOBILIARY SYSTEM     933
#     MULTIPLE ELECTROLYTES 500ML IVF      IV FLUIDS, ELECTROLYTES, TPN  INTRAVENOUS & OTHER STERILE SOLUTIONS       919

#     MYCOPHENOLATE MOFETIL 250MG/ML SUSP  SYRUP & SUSPENSION            IMMUNOLOGY                                    0
#     TORASEMIDE 20MG                      TABLETS & CAPSULES            CARDIOVASCULAR & HEMATOPOIETIC SYSTEM         0
#     TORASEMIDE 40MG TAB                  TABLETS & CAPSULES            CARDIOVASCULAR & HEMATOPOIETIC SYSTEM         0
#     MULTI VITAMINS 15ML DROPS            DROPS                         VITAMINS & MINERALS                           0
#     MEROPENEM 250MG INJ                  INJECTIONS                    ANTI-INFECTIVES                               0
#     Name: Quantity, Length: 758, dtype: int64



# total sales for each drugname in each month:
total_sales_per_month_drug=medical_dataset.groupby(['month','DrugName'])['Final_Sales'].sum()
total_sales_per_month_drug=total_sales_per_month_drug.sort_values(ascending=False)
print(total_sales_per_month_drug)
# output:
    # month  DrugName                         
    # 12     HUMAN ALBUMIN 25% INJ                44074.800
    #        PEMBROLIZUMAB                        39490.000
    #        LIPOSOMAL AMPHOTERICIN B 50MG INJ    36864.400
    # 8      MEROPENEM 1GM INJ                    34636.208
    # 11     HUMAN ALBUMIN 25% INJ                34280.400
       
    #        ADENOSINE 6MG/2ML INJ                    0.000
    # 2      DICLOFENAC 1ML INJ                       0.000
    # 5      PANTOPRAZOLE 40MG TAB                    0.000
    # 10     URSODEOXYCHOLIC ACID 300MG TAB           0.000
    # 9      CASPOFUNGIN 70MG                         0.000
    # Name: Final_Sales, Length: 3081, dtype: float64
    
    
# Calculate the percentage of missing values for 'Formulation'
total_rows=len(medical_dataset)
missing_value_Formulation=medical_dataset['Formulation'].isnull().sum()
print(missing_value_Formulation)
percentage_missing_Formulation=(missing_value_Formulation/total_rows)*100
percentage_missing_Formulation=round(percentage_missing_Formulation,2)
print("Percentage of Formulation missing:", percentage_missing_Formulation)
# output:
    # Percentage of Formulation missing: 4.59

# Calculate the percentage of missing values for 'DrugName'
total_rows=len(medical_dataset)
missing_value_Drug=medical_dataset['DrugName'].isnull().sum()
print(missing_value_Drug)
percentage_missing_Drug=(missing_value_Drug/total_rows)*100
percentage_missing_Drug=round(percentage_missing_Drug,2)
print("Percentage of drug missing:", percentage_missing_Drug)
# output:
    # Percentage of drug missing: 11.73


# Calculate the percentage of missing values for SubCat
total_rows=len(medical_dataset)
missing_value_SubCat=medical_dataset['SubCat'].isnull().sum()
print(missing_value_SubCat)
percentage_missing_SubCat=(missing_value_SubCat/total_rows)*100
percentage_missing_SubCat=round(percentage_missing_SubCat,2)
print("Percentage of SubCat missing:", percentage_missing_SubCat)
# output:
    # Percentage of SubCat missing: 11.73

# Calculate the percentage of missing values for SubCat1
total_rows=len(medical_dataset)
missing_value_SubCat1=medical_dataset['SubCat1'].isnull().sum()
print(missing_value_SubCat1)
percentage_missing_SubCat1=(missing_value_SubCat1/total_rows)*100
percentage_missing_SubCat1=round(percentage_missing_SubCat1,2)
print("Percentage of SubCat1 missing:", percentage_missing_SubCat1)
# output:
    # Percentage of SubCat1 missing: 11.9
   

total_customers=medical_dataset[(medical_dataset['Typeofsales']=='Sale')|(medical_dataset['Typeofsales']=='Return')]['Patient_ID'].nunique()
returned_customers=medical_dataset[(medical_dataset['Typeofsales']=='Return')&(medical_dataset['Final_Sales']==0)]['Patient_ID'].nunique()
bounce_rate=(returned_customers/total_customers)*100
print("bounce_rate",round(bounce_rate,2),"%")
# output:
    # bounce_rate 24.92 %
    
# The bounce rate is calculated as the percentage of customers who made returns with 
# zero final sales out of the total number of customers who made purchases or returns.
# The calculated bounce rate is approximately 24.92%.
# The bounce rate indicates that around 24.92% of customers who engaged with the sales data
# in the medical dataset made returns with zero final sales.   



returned_without_sale=medical_dataset[(medical_dataset['Final_Sales']==0)&(medical_dataset['Typeofsales']=='Return')]
drug_count=returned_without_sale.groupby(['SubCat','SubCat1'])['DrugName'].nunique()
drug_count=drug_count.sort_values(ascending=False)
print(drug_count)
# output:
    # SubCat                        SubCat1                                                           
    # INJECTIONS                    ANTI-INFECTIVES                                                       32
    #                               CARDIOVASCULAR & HEMATOPOIETIC SYSTEM                                 26
    # IV FLUIDS, ELECTROLYTES, TPN  INTRAVENOUS & OTHER STERILE SOLUTIONS                                 18
    # TABLETS & CAPSULES            CARDIOVASCULAR & HEMATOPOIETIC SYSTEM                                 15
    # INJECTIONS                    CENTRAL NERVOUS SYSTEM                                                12
    # TABLETS & CAPSULES            CENTRAL NERVOUS SYSTEM                                                11
    #                               GASTROINTESTINAL & HEPATOBILIARY SYSTEM                               10
    # INHALERS & RESPULES           RESPIRATORY SYSTEM                                                     9
    # TABLETS & CAPSULES            ENDOCRINE & METABOLIC SYSTEM                                           8
    # INJECTIONS                    ANAESTHETICS                                                           8
    #                               INTRAVENOUS & OTHER STERILE SOLUTIONS                                  8
    #                               GASTROINTESTINAL & HEPATOBILIARY SYSTEM                                7
    #                               HORMONES                                                               6
    # TABLETS & CAPSULES            ANTI-INFECTIVES                                                        6
    #                               VITAMINS & MINERALS                                                    5
    # OINTMENTS, CREAMS & GELS      DERMATOLOGY                                                            5
    # SYRUP & SUSPENSION            GASTROINTESTINAL & HEPATOBILIARY SYSTEM                                4
    # LIQUIDS & SOLUTIONS           GASTROINTESTINAL & HEPATOBILIARY SYSTEM                                3
    # SYRUP & SUSPENSION            CENTRAL NERVOUS SYSTEM                                                 3
    # NUTRITIONAL SUPPLEMENTS       NUTRITION                                                              3
    # DROPS                         OPHTHALMOLOGY                                                          3
    # POWDER                        NUTRITION                                                              3
    # INJECTIONS                    VITAMINS & MINERALS                                                    3
    #                               RESPIRATORY SYSTEM                                                     3
    # IV FLUIDS, ELECTROLYTES, TPN  NUTRITION                                                              2
    # POWDER                        GASTROINTESTINAL & HEPATOBILIARY SYSTEM                                2
    # INJECTIONS                    MUSCULO-SKELETAL SYSTEM                                                2
    # TABLETS & CAPSULES            GENITO-URINARY SYSTEM                                                  2
    #                               HORMONES                                                               2
    #                               IMMUNOLOGY                                                             2
    #                               MUSCULO-SKELETAL SYSTEM                                                2
    # PESSARIES & SUPPOSITORIES     CENTRAL NERVOUS SYSTEM                                                 2
    #                               GASTROINTESTINAL & HEPATOBILIARY SYSTEM                                2
    # TABLETS & CAPSULES            RESPIRATORY SYSTEM                                                     2
    # VACCINE                       IMMUNOLOGY                                                             2
    # SYRUP & SUSPENSION            IMMUNOLOGY                                                             1
    #                               HORMONES                                                               1
    # DROPS                         GASTROINTESTINAL & HEPATOBILIARY SYSTEM                                1
    # POWDER                        ENDOCRINE & METABOLIC SYSTEM                                           1
    # INJECTIONS                    IMMUNOLOGY                                                             1
    # DROPS                         RESPIRATORY SYSTEM                                                     1
    #                               VITAMINS & MINERALS                                                    1
    # INHALERS & RESPULES           ANTI-INFECTIVES                                                        1
    # INJECTIONS                    ANTIDOTES, DETOXIFYING AGENTS & DRUGS USED IN SUBSTANCE DEPENDENCE     1
    #                               CARDIIVASCULAR&HEMATOPOIETIC SYSTEM                                    1
    #                               ENDOCRINE & METABOLIC SYSTEM                                           1
    #                               NUTRITION                                                              1
    # POWDER                        DERMATOLOGY                                                            1
    # IV FLUIDS, ELECTROLYTES, TPN  ANTI-INFECTIVES                                                        1
    # LIQUIDS & SOLUTIONS           EAR & MOUTH/ THROAT                                                    1
    #                               RESPIRATORY SYSTEM                                                     1
    # OINTMENTS, CREAMS & GELS      ANAESTHETICS                                                           1
    #                               VITAMINS & MINERALS                                                    1
    # PATCH                         CENTRAL NERVOUS SYSTEM                                                 1
    # LOTIONS                       DERMATOLOGY                                                            1
    # Name: DrugName, dtype: int64

# The 'INJECTIONS' subcategory has the highest number of returned drugs across various 'SubCat1' categories, with 
# 'ANTI-INFECTIVES' and 'CARDIOVASCULAR & HEMATOPOIETIC SYSTEM' being the most common.


