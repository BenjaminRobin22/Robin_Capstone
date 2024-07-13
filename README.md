# Robin_Capstone
GitHub https://github.com/BenjaminRobin22/Robin_Capstone
Overleaf Report https://www.overleaf.com/read/qyrhyngwpgpd#6e6bf8
Kaggle Dataset https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who

Ben Robin's Data Science July 2024 Capstone Project Summer 2024. Identifying Factors That Affect Life Expectancy.

## Stage 1 
Downloaded the source file from Kaggle and ran data attribute analyis on it with MetaData.py
Result was an image that analysed 20 columns with the use of pandas, matplotlib and  seaborn

## Stage 2 
Cleaned the data  MetaData.iphnb
Imported region and sub-region and merged it into the data. Used Juptyter notebooks to clean the data. 
Dropped full columns Population, GDP, Hepatitis B, and Total Expenditure as there columns had too many missing rows to use. The loss of Population and GDP really hurt as these are valueable data points. I will try to find another source for these and reincorporate them into the data set.
Cleared up other columns using average by country, year, and or subregion. 
South Sudan and Sudan had more data issues than any other country but we were able to work around them. 
Also had some issues with the education columns but was able to fill them in a sufficient way. 
Dropped 10 rows for countries that only had one year entry. Not sure why they were only entered for one specific year (all the same year) but this would not work with my analysis. All of the countries were micro nations and should not effect the result when missing. 
The end result is 20 columns with complete data and no null values. 

Steps
1. Import of the data. 
2. Removing micro nations with only one year of data.
3. Adding in region and sub-region.
4. Defining null counts and addressing them.
5. Dropping columns that can not be used. 
6. Cleaning remaining columns
7. Printing cleaned dataset to CSV  

## Stage 3 
Exploratory Data Analysis (EDA) 
Taking a deeper look at the data to identify trends and distribution. There are also some more transformation steps here to put the data in a format that we can analyse it in more effectivly. 

Steps
1. Importing cleaned file form the ETL phase
2. Adding population back into the data set and calculating per capita stats
3. Visulizing data distribution relationally
4. Exposing trends in the data. Looking for direct relationships with life expectancty from dependant variables
5. Printing final data set so it is avaliable for machine learning phase