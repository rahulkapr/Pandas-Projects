import os
import pandas as pd

# Get the folder where this Python file is located
folder = os.path.dirname(os.path.abspath(__file__))

# Create the path to employee_salary.csv
file_path = os.path.join(folder, "employee_salary.csv")

# Read the CSV file
df = pd.read_csv(file_path)

print("Display the first 5 rows")
print(df.head())

print("Display the last 5 rows")
print(df.tail())

print("Dataset Information")
df.info()

print("Missing values")
print(df.isnull().sum())

print("Missing values fillup by using the median")
numerical_columns = df.select_dtypes(include="number").columns

for col in numerical_columns:
    df[col] = df[col].fillna(df[col].median())

print(df.isnull().sum())

print("Highest Salary")
highest_salary = df["Salary"].max()
print(highest_salary)

print("Lowest Salary")
lowest_salary = df["Salary"].min()
print(lowest_salary)

print("Average Salary")
average_salary = df["Salary"].mean()
print(average_salary)

print("Employees earning more than Rs. 60000")
high_salary = df[df["Salary"] > 60000]
print(high_salary[["Employee_ID", "Name", "Department", "Salary"]])

print("Employees in IT Department")
it_employees = df[df["Department"] == "IT"]
print(it_employees[["Employee_ID", "Name", "Department", "Salary"]])

print("Count employees in each department")
department_count = df["Department"].value_counts()
print(department_count)

print("Average Salary by Department")
average_department_salary = df.groupby("Department")["Salary"].mean()
print(average_department_salary)

print("Employees sorted by salary from highest to lowest")
df = df.sort_values(by="Salary", ascending=False)
print(df[["Employee_ID", "Name", "Department", "Salary"]])

print("Top 5 Highest-Paid Employees")
top_5 = df.head(5)
print(top_5[["Employee_ID", "Name", "Department", "Salary"]])

print("Employees with more than 5 years of experience")
experienced_employees = df[df["Experience"] > 5]
print(experienced_employees[
    ["Employee_ID", "Name", "Experience", "Department", "Salary"]
])

# Save cleaned CSV in the same folder
output_file = os.path.join(folder, "cleaned_employee_salary.csv")
df.to_csv(output_file, index=False)

print("Cleaned dataset saved successfully!")