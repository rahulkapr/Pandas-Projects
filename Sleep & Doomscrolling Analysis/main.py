import pandas as pd
import os

# Get the folder where main.py is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the CSV file
csv_file = os.path.join(current_folder, "sleep_doomscrolling_habits.csv")

# Read the CSV file
df = pd.read_csv(csv_file)

# Display the first 5 rows
print("Display the first 5 rows:")
print(df.head())

# Display the last 5 rows
print("\nDisplay the last 5 rows:")
print(df.tail())

# Display the shape of the dataset
rows, columns = df.shape

print("\nShape of the dataset:")
print("Number of rows:", rows)
print("Number of columns:", columns)