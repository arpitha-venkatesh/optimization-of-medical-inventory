CREATE DATABASE OMP;
USE OMP;
SELECT * FROM omp.medical_dataset;
-- converting the 'Dateofbill' column, which presumably contains date values stored as strings (objects),
-- into the DATE data type:
select * from medical_dataset;
SET SQL_SAFE_UPDATES = 0;
UPDATE medical_dataset 
SET Dateofbill = STR_TO_DATE(Dateofbill, '%m-%d-%Y');
UPDATE medical_dataset 
SET Dateofbill = 
    CASE
        WHEN INSTR(Dateofbill, '/') > 0 THEN STR_TO_DATE(Dateofbill, '%m/%d/%Y')
        ELSE STR_TO_DATE(Dateofbill, '%m-%d-%Y')
    END;

ALTER TABLE medical_dataset 
MODIFY COLUMN Dateofbill DATE;

-- The DESCRIBE statement provides metadata about the structure of the 'medical_dataset' table,
-- including details such as column names, data types, and any constraints applied to the columns.
DESCRIBE medical_dataset;

-- EDA(EXPLORATORY DATA ANALYSIS):
-- 1ST MOMENT BUSINESS DECISION:
-- MEAN:
SELECT ROUND(AVG(Quantity),3) AS mean_quantity,
       ROUND(AVG(ReturnQuantity),3) AS mean_returnquantity,
       ROUND(AVG(Final_Cost),3) AS mean_final_cost,
	   ROUND(AVG(Final_sales),3) AS mean_final_sales,
	   ROUND(AVG(RtnMRP),3) AS mean_rtnmrp FROM medical_dataset;
 --       mean_quantity:2.232	
 --       mean_returnquantity:0.292	
 -- 	  mean_final_cost:124.824	 
 --       mean_final_sales:234.038 	
--        mean_rtnmrp:29.127


-- MEDIAN:
WITH CTE AS(
SELECT quantity,ROW_NUMBER() OVER(ORDER BY quantity) as row_num,
COUNT(*) OVER() AS total_count
FROM medical_dataset)
SELECT ROUND(AVG(quantity),3) AS median_quantity
FROM CTE 
WHERE row_num IN (FLOOR((total_count+1)/2),CEIL((total_count+1)/2));
-- median_quantity:1.000


WITH CTE AS(
SELECT ReturnQuantity,ROW_NUMBER() OVER(ORDER BY ReturnQuantity) as row_num,
COUNT(*) OVER() AS total_count
FROM medical_dataset)
SELECT ROUND(AVG(ReturnQuantity),3) AS median_ReturnQuantity
FROM CTE 
WHERE row_num IN (FLOOR((total_count+1)/2),CEIL((total_count+1)/2));
-- median_ReturnQuantity:0.000

WITH CTE AS(
SELECT Final_Cost,ROW_NUMBER() OVER(ORDER BY Final_Cost) as row_num,
COUNT(*) OVER() AS total_count
FROM medical_dataset)
SELECT ROUND(AVG(Final_Cost),3) AS median_Final_Cost
FROM CTE 
WHERE row_num IN (FLOOR((total_count+1)/2),CEIL((total_count+1)/2));
-- median_Final_Cost:53.65

WITH CTE AS(
SELECT Final_sales,ROW_NUMBER() OVER(ORDER BY Final_sales) as row_num,
COUNT(*) OVER() AS total_count
FROM medical_dataset)
SELECT ROUND(AVG(Final_sales),3) AS median_Final_sales
FROM CTE 
WHERE row_num IN (FLOOR((total_count+1)/2),CEIL((total_count+1)/2));
-- median_Final_sales:86.424

WITH CTE AS(
SELECT RtnMRP,ROW_NUMBER() OVER(ORDER BY RtnMRP) as row_num,
COUNT(*) OVER() AS total_count
FROM medical_dataset)
SELECT ROUND(AVG(RtnMRP),3) AS median_RtnMRP
FROM CTE 
WHERE row_num IN (FLOOR((total_count+1)/2),CEIL((total_count+1)/2));
-- median_RtnMRP:0

-- MODE:
WITH CTE AS(
SELECT *, COUNT(Typeofsales) OVER(PARTITION BY Typeofsales)
AS ranked FROM medical_dataset)
SELECT DISTINCT(Typeofsales) AS mode_Typeofsales FROM CTE 
WHERE ranked=(SELECT MAX(ranked) FROM CTE);
-- mode_Typeofsales:Sale

WITH CTE AS(
SELECT *, COUNT(Specialisation) OVER(PARTITION BY Specialisation)
AS ranked FROM medical_dataset)
SELECT DISTINCT(Specialisation) AS mode_Specialisation FROM CTE 
WHERE ranked=(SELECT MAX(ranked) FROM CTE);
-- mode_Specialisation:Specialisation4

WITH CTE AS(
SELECT *, COUNT(Dept) OVER(PARTITION BY Dept)
AS ranked FROM medical_dataset)
SELECT DISTINCT(Dept) AS mode_Dept FROM CTE 
WHERE ranked=(SELECT MAX(ranked) FROM CTE);
-- mode_Dept:Department1

WITH CTE AS(
SELECT *, COUNT(Formulation) OVER(PARTITION BY Formulation)
AS ranked FROM medical_dataset)
SELECT DISTINCT(Formulation) AS mode_Formulation FROM CTE 
WHERE ranked=(SELECT MAX(ranked) FROM CTE);
-- mode_Formulation:Form1

WITH CTE AS(
SELECT *, COUNT(DrugName) OVER(PARTITION BY DrugName)
AS ranked FROM medical_dataset)
SELECT DISTINCT(DrugName) AS mode_DrugName FROM CTE 
WHERE ranked=(SELECT MAX(ranked) FROM CTE);
-- mode_DrugName:SODIUM CHLORIDE IVF 100ML

WITH CTE AS(
SELECT *, COUNT(Subcat) OVER(PARTITION BY Subcat)
AS ranked FROM medical_dataset)
SELECT DISTINCT(Subcat) AS mode_Subcat FROM CTE 
WHERE ranked=(SELECT MAX(ranked) FROM CTE);
-- mode_Subcat:INJECTIONS

WITH CTE AS(
SELECT *, COUNT(Subcat1) OVER(PARTITION BY Subcat1)
AS ranked FROM medical_dataset)
SELECT DISTINCT(Subcat1) AS mode_Subcat1 FROM CTE 
WHERE ranked=(SELECT MAX(ranked) FROM CTE);
-- mode_Subcat1:INTRAVENOUS & OTHER STERILE SOLUTIONS

-- second moment of bussiness understanding(measure of dispersion):
-- variance:
SELECT ROUND(VARIANCE(Quantity),3) as variance_quantity ,
ROUND(VARIANCE(ReturnQuantity),3) as variance_ReturnQuantity ,
ROUND(VARIANCE(Final_cost),3) as variance_Final_cost,
ROUND(VARIANCE(Final_Sales),3) as variance_Finale_Sales ,
ROUND(VARIANCE(RtnMRP),3) as variance_RtnMRP FROM medical_dataset;
-- variance_quantity:26.336	
-- variance_ReturnQuantity:2.7	
-- variance_Final_cost:216007.852	
-- Finale_Sales:450560.406	
-- variance_RtnMRP:33217.222

-- standard deviation:
SELECT ROUND(STD(Quantity),3) as std_dev_quantity,
 ROUND(STD(ReturnQuantity),3) as std_dev_ReturnQuantity,
 ROUND(STD(Final_cost),3) as std_dev_Final_cost,
 ROUND(STD(Final_Sales),3) as std_dev_Final_Sales,
 ROUND(STD(RtnMRP),3) as std_dev_RtnMRP FROM medical_dataset;
 -- std_dev_quantity:5.132	
 -- std_dev_ReturnQuantity:1.643	
 -- std_dev_Final_cost:464.766	
 -- std_dev_Final_Sales:671.238	
 -- std_dev_RtnMRP:182.256

-- range:
SELECT MAX(Quantity)-MIN(Quantity) AS range_Quantity,
MAX(ReturnQuantity)-MIN(ReturnQuantity) AS range_ReturnQuantity,
MAX(final_cost)-MIN(final_cost) AS range_final_cost,
MAX(Final_Sales)-MIN(Final_Sales) AS range_Final_Sales,
MAX(RtnMRP)-MIN(RtnMRP) AS range_RtnMRP FROM medical_dataset;
-- range_Quantity:150	
-- range_ReturnQuantity:50	
-- range_final_cost:33138	
-- range_Final_Sales:39490	
-- range_RtnMRP:8014

-- third moment of bussiness understanding:
-- skewness:
SELECT ROUND(SUM(POWER(Quantity-(SELECT AVG(Quantity) FROM medical_dataset),3))
/COUNT(Quantity)/POWER((SELECT STD(Quantity) FROM medical_dataset),3),3) AS skewness_Quantity ,
ROUND(SUM(POWER(ReturnQuantity-(SELECT AVG(ReturnQuantity) FROM medical_dataset),3))
/COUNT(ReturnQuantity)/POWER((SELECT STD(ReturnQuantity) FROM medical_dataset),3),3) AS skewness_ReturnQuantity,
ROUND(SUM(POWER(final_cost-(SELECT AVG(final_cost) FROM medical_dataset),3))
/COUNT(final_cost)/POWER((SELECT STD(final_cost) FROM medical_dataset),3),3) AS skewness_final_cost, 
ROUND(SUM(POWER(Final_Sales-(SELECT AVG(Final_Sales) FROM medical_dataset),3))
/COUNT(Final_Sales)/POWER((SELECT STD(Final_Sales) FROM medical_dataset),3),3) AS skewness_Final_Sales,
ROUND(SUM(POWER(RtnMRP-(SELECT AVG(RtnMRP) FROM medical_dataset),3))
/COUNT(RtnMRP)/POWER((SELECT STD(RtnMRP) FROM medical_dataset),3),3) AS skewness_RtnMRP
FROM medical_dataset;
-- skewness_Quantity:11.34	
-- skewness_ReturnQuantity:17.171	
-- skewness_final_cost:34.505	
-- skewness_Final_Sales:21.005	
-- skewness_RtnMRP:15.796

-- forth moment of bussiness understanding
-- kurtosis:
SELECT  ROUND(SUM(POWER(Quantity-(SELECT AVG(Quantity) FROM medical_dataset),4))
/COUNT(Quantity)/POWER((SELECT STD(Quantity) FROM medical_dataset),4)-3,3) AS kurtosis_Quantity,
ROUND(SUM(POWER(ReturnQuantity-(SELECT AVG(ReturnQuantity) FROM medical_dataset),4))
/COUNT(ReturnQuantity)/POWER((SELECT STD(ReturnQuantity) FROM medical_dataset),4)-3,3) AS kurtosis_ReturnQuantity,
ROUND(SUM(POWER(final_cost-(SELECT AVG(final_cost) FROM medical_dataset),4))
/COUNT(final_cost)/POWER((SELECT STD(final_cost) FROM medical_dataset),4)-3,3) AS kurtosis_final_cost,
ROUND(SUM(POWER(final_sales-(SELECT AVG(final_sales) FROM medical_dataset),4))
/COUNT(final_sales)/POWER((SELECT STD(final_sales) FROM medical_dataset),4)-3,3) AS kurtosis_final_sales, 
ROUND(SUM(POWER(RtnMRP-(SELECT AVG(RtnMRP) FROM medical_dataset),4))
/COUNT(RtnMRP)/POWER((SELECT STD(RtnMRP) FROM medical_dataset),4)-3,3) AS kurtosis_RtnMRP 
FROM medical_dataset;
-- kurtosis_Quantity:180.09	
-- kurtosis_ReturnQuantity:409.273	
-- kurtosis_final_cost:2025.154	
-- kurtosis_final_sales:948.189	
-- kurtosis_RtnMRP:403.383



-- TOTAL NUMBER OF QUANTITY SOLD FOR EACH WEEK
select week(Dateofbill) as week,sum(quantity) as total_quantity_sold
from medical_dataset 
group by week(dateofbill) 
order by total_quantity_sold desc;
-- Week 9 had the highest total quantity sold, with 998 units.
-- The top weeks with the highest total quantity sold also include weeks 50, 27, 30, and 51, ranging from 881 to 752 units.
-- Week 2 had the lowest total quantity sold, with only 358 units.
-- Week 0 seems to have an unusually low total quantity sold, with only 50 units.


-- TOTAL NUMBER OF QUANTITY SOLD FOR EACH MONTH
select month(Dateofbill) as month,sum(quantity) as total_quantity_sold 
from medical_dataset 
group by month(dateofbill)
order by total_quantity_sold desc;
-- December (Month 12) had the highest total quantity sold, with 3,105 units.
-- Following December, July (Month 7) and August (Month 8) had the next highest total quantity sold, 
-- with 3,010 and 2,983 units respectively.
-- There's a noticeable decrease in total quantity sold from July to February, with February (Month 2) and June (Month 6) 
-- having the lowest total quantity sold among the listed months, at 2,123 and 2,126 units respectively.

-- TOTAL NUMBER OF QUANTITY RETURN FOR EACH WEEK
select week(Dateofbill) as week,sum(returnquantity) as total_quantity_return
from medical_dataset 
group by week(dateofbill) 
order by  total_quantity_return desc;
-- Week 33 had the highest total quantity returned, with 195 units.
-- Following Week 33, Week 5 and Week 18 had the next highest total quantity returned, with 150 and 148
 -- units respectively.
-- Week 39 had the lowest total quantity returned, with only 31 units.

-- TOTAL NUMBER OF QUANTITY RETURN FOR EACH MONTH
select month(Dateofbill) as month,sum(returnquantity) as total_quantity_return
from medical_dataset 
group by month(dateofbill)
order by total_quantity_return desc;
-- Month 8 (August) had the highest total quantity returned, with 558 units.
-- Following August, Month 5 (May) and Month 11 (November) had the next highest total quantity returned, 
-- with 470 and 384 units respectively.
-- Month 10 (October) had the lowest total quantity returned, with only 244 units.

-- Drug with the highest total quantity sold
select drugname,sum(quantity) as total_quantity_sold
from medical_dataset
group by drugname
order by total_quantity_sold desc;
--  drug "Sodium Chloride IVF 100ML" has sold the most with a total quantity sold of 1278 units.
-- and Among the total quantity sold, there are 8266 units with missing values.

-- Total quantity sold for each drug per month
select drugname,month(dateofbill), sum(quantity) as total_quantity_sold
from medical_dataset
group by drugname,month(dateofbill)
order by total_quantity_sold desc;
-- Due to missing values in the 'drugname' column, we are unable to determine which drug has the total_quantity_sold per month.

-- Total quantity sold for each drug per week
select drugname,week(dateofbill), sum(quantity) as total_quantity_sold
from medical_dataset
group by drugname,week(dateofbill)
order by total_quantity_sold desc;
-- Due to missing values in the 'drugname' column, we are unable to determine which drug has the total_quantity_sold per week.


-- Drug,subcat,subcat1 with the highest total sales quantity
select drugname,subcat,subcat1,sum(quantity) as total_quantity_sold
from medical_dataset
group by drugname,subcat,subcat1
order by total_quantity_sold desc;
-- there are missing values in the drug column,  having a total quantity sold of 8266 units.


-- total sales per month 
select month(dateofbill)as month,round(sum(final_Sales),3) as total_Sales 
from medical_dataset
group by month(dateofbill) 
order by  total_Sales desc;
-- December (Month 12) has the highest total sales of approximately 412259.126.
-- This is followed by August (Month 8) with total sales of approximately 319996.63, 
-- and July (Month 7) with approximately 309785.63 in sales.
-- June (Month 6) has the lowest total sales of approximately 216637.552

-- total sales per week
select week(dateofbill)as month,round(sum(final_Sales),3) as total_Sales 
from medical_dataset
group by week(dateofbill) 
order by total_Sales desc;
-- Week 50 has the highest total sales of approximately 107002.59, followed closely by Week 52 with approximately 103689.934 in sales.
-- Week 0 has the lowest sales of 4999.75.

-- total sales for each drugname in each month from the medical_dataset table
select month(dateofbill) as month,drugname, sum(final_sales) as total_sales
from medical_dataset
group by month(dateofbill),drugname
order by total_sales desc;
-- Due to missing values in the 'drugname' column, we are unable to determine which drug has the total_sales per month.


-- total sales for each drugname in each week from the medical_dataset table
select week(dateofbill) as week,drugname, sum(final_sales) as total_sales
from medical_dataset
group by week(dateofbill),drugname
order by total_sales desc;
-- Due to missing values in the 'drugname' column, we are unable to determine which drug has the total_sales per week.

select (count(case when drugname is null then 1 end)*100.0)/count(*) as percentage_missing_drugname
from medical_dataset;
-- percentage_missing_drugname: 11.73161

select (count(case when SubCat is null then 1 end)*100.0)/count(*) as percentage_missing_SubCat
from medical_dataset;
-- percentage_missing_SubCat:11.73161

select (count(case when SubCat1 is null then 1 end)*100.0)/count(*) as percentage_missing_SubCat1
from medical_dataset;
-- percentage_missing_SubCat1:11.90041

select (count(case when Formulation is null then 1 end)*100.0)/count(*) as percentage_missing_Formulation
from medical_dataset;
-- percentage_missing_Formulation:4.59277

    
-- calculates the bounce rate for customers based on the sales data in the medical_dataset
select round((bounced_customer/total_customer)*100,2) as bounce_rate
from
(select count(distinct Patient_id) as total_customer
from medical_dataset
where typeofsales in('sale','return')) as a,
(select count(distinct Patient_ID) as bounced_customer
from medical_dataset
where typeofsales='return' and final_Sales=0) as b;
-- bounce_rate:24.92
-- bounce rate indicates that about 24.92% of customers who made purchases ended up returning items 
-- with zero final sales, suggesting potential issues with product satisfaction, quality, or 
-- fulfillment processes that might be contributing to returns without purchases.

-- calculate the number of drugs in each subcat,subcat1 that have been returned without making a sale (Final_Sales = 0).
 SELECT SubCat,subcat1, COUNT(DISTINCT DrugName) AS num_returned_drugs
FROM medical_dataset
WHERE Typeofsales = 'Return' AND Final_Sales = 0
GROUP BY SubCat,subcat1
ORDER BY num_returned_drugs DESC;
-- the combination of sub-categories "INJECTIONS" and 
-- sub-category2 "ANTI-INFECTIVES" has the highest count of returned drugs, with 32 distinct drugs.









