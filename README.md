# Customer Personality Analysis – Data Cleaning & Preprocessing
This project performs data cleaning and preprocessing on the marketing_campaign.csv dataset, which contains information about customer demographics and behavior. The script is written in Python using Pandas for data manipulation and cleaning.

Dataset:
File: marketing_campaign.csv

Format: Tab-separated (.csv)

Source: Customer marketing and personality analysis data

 Key Cleaning Steps
Handled missing values in the Income column by dropping rows.

Removed duplicate rows.

Standardized text entries in Education and Marital_Status.

Consolidated inconsistent marital status categories (e.g., widow, alone → single).

Converted Dt_Customer to datetime format (dd-mm-yyyy).

Renamed all column headers to lowercase with underscores.

Ensured proper data types for id, kidhome, teenhome, and complain.

Requirements
Python 3.x

pandas

How to Run : python clean_marketing_data.py
