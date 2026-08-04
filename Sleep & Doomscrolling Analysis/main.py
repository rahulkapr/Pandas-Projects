import pandas as pd
import os
# Get the folder where main.py is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the CSV file
csv_file = os.path.join(current_folder, "sleep_doomscrolling_habits.csv")

# Read the CSV file
df = pd.read_csv(csv_file)

print("..............BEGINNER LEVEL...............")


#Display the first 5 rows.
print("Display the first 5 rows:")
print(df.head())

#Display the last 5 rows.
print("\nDisplay the last 5 rows:")
print(df.tail())

# Display the shape of the dataset
rows, columns = df.shape

print("\nShape of the dataset:")

#Number of rows
print("Number of rows:", rows)

#Number of columns
print("Number of columns:", columns)

#Display all column names.
print("ALL Clumns Names")
for column in df.columns:
    print(column)


#Check the data types of every column.
print("Data types of every column")
for column in df.columns:
    print(column, ":", df[column].dtypes)


#Display dataset information.
print("Dataset Information")
print(df.info())    

#Generate descriptive statistics.
print("Descriptive Statistics")
print(df.describe())


#Check for missing values.
print("Missing Values")
print(df.isnull().sum())


#Count missing values in each column.
print("Count missing values in each column")
for column in df.columns:
    print(column, ":", df[column].isnull().sum())