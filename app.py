import pandas as pd

# Load the dataset
try:
    df = pd.read_csv('marketing_campaign.csv', sep='\t')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: marketing_campaign.csv not found. Please make sure the file is in the correct directory.")
    exit()

# --- Initial Data Exploration ---
print("\n--- Initial Information ---")
df.info()
print("\n--- First 5 Rows ---")
print(df.head())
print("\n--- Descriptive Statistics ---")
print(df.describe(include='all'))
print("\n--- Unique Values in Key Columns ---")
for col in ['Education', 'Marital_Status', 'Income', 'Kidhome', 'Teenhome', 'Complain']:
    print(f"\nUnique values in '{col}': {df[col].unique()}")

# --- Data Cleaning and Preprocessing ---

# 1. Handle Missing Values
print("\n--- Handling Missing Values ---")
print(f"Number of missing values before: {df.isnull().sum().sum()}")
# Income seems to have missing values. Let's investigate.
print("\nRows with missing Income:")
print(df[df['Income'].isnull()])
# Since Income is important, and the number of missing values isn't huge,
# we might consider imputation. For simplicity in this example, let's drop these rows.
df_cleaned = df.dropna(subset=['Income']).copy()
print(f"Number of missing values after dropping rows with missing Income: {df_cleaned.isnull().sum().sum()}")

# 2. Remove Duplicate Rows
print("\n--- Handling Duplicates ---")
print(f"Number of duplicate rows before: {df_cleaned.duplicated().sum()}")
df_cleaned.drop_duplicates(inplace=True)
print(f"Number of duplicate rows after: {df_cleaned.duplicated().sum()}")

# 3. Standardize Text Values
print("\n--- Standardizing Text Values ---")
# Education
print(f"\nUnique values in 'Education' before: {df_cleaned['Education'].unique()}")
df_cleaned['Education'] = df_cleaned['Education'].str.lower()
print(f"Unique values in 'Education' after: {df_cleaned['Education'].unique()}")

# Marital_Status
print(f"\nUnique values in 'Marital_Status' before: {df_cleaned['Marital_Status'].unique()}")
df_cleaned['Marital_Status'] = df_cleaned['Marital_Status'].str.lower().replace({'divorced':'separated', 'widow':'single', 'alone':'single', 'absurd':'other', 'yolo':'other'})
print(f"Unique values in 'Marital_Status' after: {df_cleaned['Marital_Status'].unique()}")

# 4. Convert Date Formats
print("\n--- Converting Date Formats ---")
print(f"Data type of 'Dt_Customer' before: {df_cleaned['Dt_Customer'].dtype}")
df_cleaned['Dt_Customer'] = pd.to_datetime(df_cleaned['Dt_Customer'], format='%d-%m-%Y')
print(f"Data type of 'Dt_Customer' after: {df_cleaned['Dt_Customer'].dtype}")
print(f"Example of 'Dt_Customer' after conversion: {df_cleaned['Dt_Customer'].head()}")

# 5. Rename Column Headers
print("\n--- Renaming Column Headers ---")
print(f"Column names before: {df_cleaned.columns.tolist()}")
df_cleaned.columns = df_cleaned.columns.str.lower().str.replace(' ', '_')
print(f"Column names after: {df_cleaned.columns.tolist()}")

# 6. Check and Fix Data Types
print("\n--- Checking and Fixing Data Types ---")
print(f"Data types before:\n{df_cleaned.dtypes}")
# 'id' should be an integer
df_cleaned['id'] = df_cleaned['id'].astype(int)
# 'kidhome' and 'teenhome' seem to be integers already, but let's ensure
df_cleaned['kidhome'] = df_cleaned['kidhome'].astype(int)
df_cleaned['teenhome'] = df_cleaned['teenhome'].astype(int)
# 'complain' should likely be a boolean or integer (0/1)
df_cleaned['complain'] = df_cleaned['complain'].astype(int)
print(f"\nData types after:\n{df_cleaned.dtypes}")

# --- Final Cleaned Dataset ---
print("\n--- First 5 Rows of Cleaned Dataset ---")
print(df_cleaned.head())
print("\n--- Information of Cleaned Dataset ---")
df_cleaned.info()

# --- Summary of Changes ---
print("\n--- Summary of Changes ---")
print("- Handled missing values in 'Income' by dropping the corresponding rows.")
print("- Removed duplicate rows from the dataset.")
print("- Standardized text values in 'Education' and 'Marital_Status' to lowercase and consolidated some categories in 'Marital_Status'.")
print("- Converted the 'Dt_Customer' column to datetime objects with a consistent format.")
print("- Renamed column headers to lowercase with underscores instead of spaces for better readability.")
print("- Checked and ensured appropriate data types for 'id', 'kidhome', 'teenhome', and 'complain'.")