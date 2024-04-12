USE OMP;
drop table medical_dataset;
select * from medical_dataset;

-- PRE-PROCESSING:
-- TYPE CASTING:
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

-- DUPLICATION HANDLING:
select count(*) as total_row from medical_dataset;
-- total_row: 14218

-- finding duplicated rows in medical_dataset
SELECT 
    Typeofsales, Patient_ID, Specialisation, Dept, Dateofbill, Quantity, 
    ReturnQuantity, Final_Cost, Final_Sales, RtnMRP, Formulation, DrugName, 
    SubCat, SubCat1,COUNT(Patient_ID) AS total
FROM 
    medical_dataset 
GROUP BY 
    Typeofsales, Patient_ID, Specialisation, Dept, Dateofbill, Quantity, 
    ReturnQuantity, Final_Cost, Final_Sales, RtnMRP, Formulation, DrugName, 
    SubCat, SubCat1
HAVING 
    total > 1
LIMIT 0, 50000;

-- calculating total_duplicated_row
with duplicates as(
SELECT 
    Typeofsales, Patient_ID, Specialisation, Dept, Dateofbill, Quantity, 
    ReturnQuantity, Final_Cost, Final_Sales, RtnMRP, Formulation, DrugName, 
    SubCat, SubCat1,COUNT(Patient_ID) AS total
FROM 
    medical_dataset 
GROUP BY 
    Typeofsales, Patient_ID, Specialisation, Dept, Dateofbill, Quantity, 
    ReturnQuantity, Final_Cost, Final_Sales, RtnMRP, Formulation, DrugName, 
    SubCat, SubCat1
HAVING 
    total > 1
LIMIT 0, 50000)
select count(*) as total_duplicated_row from duplicates;
-- total_duplicated_row: 26

-- droping duplicated column in medical_dataset:
DELETE FROM medical_dataset
WHERE (Typeofsales, Patient_ID, Specialisation, Dept, Dateofbill, Quantity, 
    ReturnQuantity, Final_Cost, Final_Sales, RtnMRP, Formulation, DrugName, 
    SubCat, SubCat1) IN (
    SELECT Typeofsales, Patient_ID, Specialisation, Dept, Dateofbill, Quantity, 
    ReturnQuantity, Final_Cost, Final_Sales, RtnMRP, Formulation, DrugName, 
    SubCat, SubCat1
    FROM (
        SELECT 
            Typeofsales, Patient_ID, Specialisation, Dept, Dateofbill, Quantity, 
            ReturnQuantity, Final_Cost, Final_Sales, RtnMRP, Formulation, DrugName, 
            SubCat, SubCat1,
            ROW_NUMBER() OVER (PARTITION BY Typeofsales, Patient_ID, Specialisation, Dept, Dateofbill, Quantity, 
            ReturnQuantity, Final_Cost, Final_Sales, RtnMRP, Formulation, DrugName, 
            SubCat, SubCat1) AS rn 
        FROM 
            medical_dataset
    ) ctc
    WHERE ctc.rn > 1
);


-- handling missing value: 
-- counthing number of null value in each column:
SELECT
    SUM(CASE WHEN Typeofsales IS NULL THEN 1 ELSE 0 END) AS Typeofsales_null_count,
    SUM(CASE WHEN Patient_ID IS NULL THEN 1 ELSE 0 END) AS Patient_ID_null_count,
    SUM(CASE WHEN Specialisation IS NULL THEN 1 ELSE 0 END) AS Specialisation_null_count,
    SUM(CASE WHEN Dept IS NULL THEN 1 ELSE 0 END) AS Dept_null_count,
    SUM(CASE WHEN Dateofbill IS NULL THEN 1 ELSE 0 END) AS Dateofbill_null_count,
    SUM(CASE WHEN Quantity IS NULL THEN 1 ELSE 0 END) AS Quantity_null_count,
    SUM(CASE WHEN ReturnQuantity IS NULL THEN 1 ELSE 0 END) AS ReturnQuantity_null_count,
    SUM(CASE WHEN Final_Cost IS NULL THEN 1 ELSE 0 END) AS Final_Cost_null_count,
    SUM(CASE WHEN Final_Sales IS NULL THEN 1 ELSE 0 END) AS Final_Sales_null_count,
    SUM(CASE WHEN RtnMRP IS NULL THEN 1 ELSE 0 END) AS RtnMRP_null_count,
    SUM(CASE WHEN Formulation IS NULL THEN 1 ELSE 0 END) AS Formulation_null_count,
    SUM(CASE WHEN DrugName IS NULL THEN 1 ELSE 0 END) AS DrugName_null_count,
    SUM(CASE WHEN SubCat IS NULL THEN 1 ELSE 0 END) AS SubCat_null_count,
    SUM(CASE WHEN SubCat1 IS NULL THEN 1 ELSE 0 END) AS SubCat1_null_count
FROM
    medical_dataset;
    
    -- Typeofsales_null_count:0	
    -- Patient_ID_null_count:0	
    -- Specialisation_null_count:0	
    -- Dept_null_count:0	
    -- Dateofbill_null_count:0	
    -- Quantity_null_count:0	
    -- ReturnQuantity_null_count:0	
    -- Final_Cost_null_count:0	
    -- Final_Sales_null_count:0	
    -- RtnMRP_null_count:0	
    -- Formulation_null_count:653	
    -- DrugName_null_count:1668	
    -- SubCat_null_count:1668	
    -- SubCat1_null_count:1692

-- droping the null value in drugname column:
delete from medical_dataset 
where drugname is null;

-- after deleting null value in drugname column:
SELECT
    SUM(CASE WHEN Typeofsales IS NULL THEN 1 ELSE 0 END) AS Typeofsales_null_count,
    SUM(CASE WHEN Patient_ID IS NULL THEN 1 ELSE 0 END) AS Patient_ID_null_count,
    SUM(CASE WHEN Specialisation IS NULL THEN 1 ELSE 0 END) AS Specialisation_null_count,
    SUM(CASE WHEN Dept IS NULL THEN 1 ELSE 0 END) AS Dept_null_count,
    SUM(CASE WHEN Dateofbill IS NULL THEN 1 ELSE 0 END) AS Dateofbill_null_count,
    SUM(CASE WHEN Quantity IS NULL THEN 1 ELSE 0 END) AS Quantity_null_count,
    SUM(CASE WHEN ReturnQuantity IS NULL THEN 1 ELSE 0 END) AS ReturnQuantity_null_count,
    SUM(CASE WHEN Final_Cost IS NULL THEN 1 ELSE 0 END) AS Final_Cost_null_count,
    SUM(CASE WHEN Final_Sales IS NULL THEN 1 ELSE 0 END) AS Final_Sales_null_count,
    SUM(CASE WHEN RtnMRP IS NULL THEN 1 ELSE 0 END) AS RtnMRP_null_count,
    SUM(CASE WHEN Formulation IS NULL THEN 1 ELSE 0 END) AS Formulation_null_count,
    SUM(CASE WHEN DrugName IS NULL THEN 1 ELSE 0 END) AS DrugName_null_count,
    SUM(CASE WHEN SubCat IS NULL THEN 1 ELSE 0 END) AS SubCat_null_count,
    SUM(CASE WHEN SubCat1 IS NULL THEN 1 ELSE 0 END) AS SubCat1_null_count
FROM
    medical_dataset;
     -- Typeofsales_null_count:0	
    -- Patient_ID_null_count:0	
    -- Specialisation_null_count:0	
    -- Dept_null_count:0	
    -- Dateofbill_null_count:0	
    -- Quantity_null_count:0	
    -- ReturnQuantity_null_count:0	
    -- Final_Cost_null_count:0	
    -- Final_Sales_null_count:0	
    -- RtnMRP_null_count:0	
    -- Formulation_null_count:489
    -- DrugName_null_count:0
    -- SubCat_null_count:0	
    -- SubCat1_null_count:24

-- finding unique subat value where subcat1 is null:
select  distinct subcat from medical_dataset where subcat1 is null;
-- NUTRITIONAL SUPPLEMENTS
-- OINTMENTS, CREAMS & GELS
-- SPRAY
-- POWDER
-- TABLETS & CAPSULES

-- finding most_occured subcat1 where subcat= "NUTRITIONAL SUPPLEMENTS":
select distinct subcat1 from medical_dataset where subcat= "NUTRITIONAL SUPPLEMENTS";
-- NUTRITION

-- Replace missing values in SubCat1 with 'NUTRITION' where SubCat is 'NUTRITIONAL SUPPLEMENTS':
update medical_dataset
set subcat1='NUTRITION' 
where SubCat='NUTRITIONAL SUPPLEMENTS' and subcat1 is null;

select count(*) from medical_dataset where subcat1 is null;
-- output:12

-- finding most_occured subcat1 where subcat= "OINTMENTS, CREAMS & GELS":
SELECT SubCat1, COUNT(*) AS count
FROM medical_dataset where subcat= "OINTMENTS, CREAMS & GELS"
GROUP BY SubCat1
ORDER BY count DESC
LIMIT 1;
-- ANAESTHETICS

-- Replace missing values in SubCat1 with 'ANAESTHETICS' where SubCat is 'OINTMENTS, CREAMS & GELS':
update medical_dataset
set subcat1='ANAESTHETICS' 
where SubCat='OINTMENTS, CREAMS & GELS' and subcat1 is null;

select count(*) from medical_dataset where subcat1 is null;
-- output:4

-- finding most_occured subcat1 where subcat= "SPRAY":
SELECT SubCat1, COUNT(*) AS count
FROM medical_dataset where subcat= "SPRAY"
GROUP BY SubCat1
ORDER BY count DESC
LIMIT 1;
-- CENTRAL NERVOUS SYSTEM

-- Replace missing values in SubCat1 with 'CENTRAL NERVOUS SYSTEM' where SubCat is 'SPRAY':
update medical_dataset
set subcat1='CENTRAL NERVOUS SYSTEM' 
where SubCat='SPRAY' and subcat1 is null;

select count(*) from medical_dataset where subcat1 is null;
-- output: 2


-- finding most_occured subcat1 where subcat= "POWDER":
SELECT SubCat1, COUNT(*) AS count
FROM medical_dataset where subcat= "POWDER"
GROUP BY SubCat1
ORDER BY count DESC
LIMIT 1;
-- GASTROINTESTINAL & HEPATOBILIARY SYSTEM

-- Replace missing values in SubCat1 with 'GASTROINTESTINAL & HEPATOBILIARY SYSTEM' where SubCat is 'POWDER':
update medical_dataset
set subcat1='GASTROINTESTINAL & HEPATOBILIARY SYSTEM' 
where SubCat='POWDER' and subcat1 is null;

select count(*) from medical_dataset where subcat1 is null;
-- output:1


-- finding most_occured subcat1 where subcat= "TABLETS & CAPSULES":
SELECT SubCat1, COUNT(*) AS count
FROM medical_dataset where subcat= "TABLETS & CAPSULES"
GROUP BY SubCat1
ORDER BY count DESC
LIMIT 1;
-- CARDIOVASCULAR & HEMATOPOIETIC SYSTEM

-- Replace missing values in SubCat1 with 'CARDIOVASCULAR & HEMATOPOIETIC SYSTEM' where SubCat is 'TABLETS & CAPSULES':
update medical_dataset
set subcat1='CARDIOVASCULAR & HEMATOPOIETIC SYSTEM' 
where SubCat='TABLETS & CAPSULES' and subcat1 is null;

select count(*) from medical_dataset where subcat1 is null;
-- output:0

-- for formulation column:
-- finding unique subat value where formulation is null:
select  distinct subcat from medical_dataset where formulation is null;
-- IV FLUIDS, ELECTROLYTES, TPN
-- INJECTIONS
-- TABLETS & CAPSULES

-- finding most_occured formulation where subcat= "IV FLUIDS, ELECTROLYTES, TPN":
SELECT formulation, COUNT(*) AS count
FROM medical_dataset where subcat= "IV FLUIDS, ELECTROLYTES, TPN"
GROUP BY formulation
ORDER BY count DESC
LIMIT 1;
-- Form1

-- Replace missing values in formulation with 'Form1' where SubCat is 'IV FLUIDS, ELECTROLYTES, TPN':
update medical_dataset
set formulation='Form1' 
where SubCat='IV FLUIDS, ELECTROLYTES, TPN' and formulation is null;

select count(*) from medical_dataset where formulation is null;
-- output:280

-- finding most_occured formulation where subcat= "INJECTIONS":
SELECT formulation, COUNT(*) AS count
FROM medical_dataset where subcat= "INJECTIONS"
GROUP BY formulation
ORDER BY count DESC
LIMIT 1;
-- Form1

-- Replace missing values in formulation with 'Form1' where SubCat is 'INJECTIONS':
update medical_dataset
set formulation='Form1' 
where SubCat='INJECTIONS' and formulation is null;

select count(*) from medical_dataset where formulation is null;
-- output:11

-- finding most_occured formulation where subcat= "TABLETS & CAPSULES":
SELECT formulation, COUNT(*) AS count
FROM medical_dataset where subcat= "TABLETS & CAPSULES"
GROUP BY formulation
ORDER BY count DESC
LIMIT 1;
-- Form1

-- Replace missing values in formulation with 'Form1' where SubCat is 'TABLETS & CAPSULES':
update medical_dataset
set formulation='Form1' 
where SubCat='TABLETS & CAPSULES' and formulation is null;

select count(*) from medical_dataset where formulation is null;
-- output:0


-- zero variance:
SELECT ROUND(VARIANCE(Quantity),3) as variance_quantity ,
ROUND(VARIANCE(ReturnQuantity),3) as variance_ReturnQuantity ,
ROUND(VARIANCE(Final_cost),3) as variance_Final_cost,
ROUND(VARIANCE(Final_Sales),3) as variance_Finale_Sales ,
ROUND(VARIANCE(RtnMRP),3) as variance_RtnMRP FROM medical_dataset;
