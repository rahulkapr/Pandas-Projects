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



print("...................Data Cleaning..................")
#Remove duplicate rows.
print("Remove duplicate rows")
df=df.drop_duplicates()
print(df)

#Count duplicate rows.
print("Count duplicate rows")
print(df.duplicated().sum())



#Fill missing numerical values using:
print("Fill missing values")
#median
df_median=df.copy()
numerical_columns=df_median.select_dtypes(include="number").columns

for col in numerical_columns:
    df_median[col]=df_median[col].fillna(df_median[col].median())
print("\nMissing values after filling with Median:")
print(df_median.isnull().sum())



#Mean
df_mean=df.copy()
numerical_columns=df_mean.select_dtypes(include="number").columns

for col in numerical_columns:
    df_mean[col]=df_mean[col].fillna(df_mean[col].mean())

print("\nMissing values after filling with Median:")
print(df_mean.isnull().sum())


#Fill missing categorical values using Mode.
print("Missing categorical values using Mode")

string_colums=df.select_dtypes(include="object").columns

for col in string_colums:
    df[col]=df[col].fillna(df[col].mode()[0])

print(df[string_colums].isnull().sum())


#Rename one or more columns.
print("Remane one or more columns")
df.rename(columns={"respondent_id":"ID"}, inplace=True)
print(df.columns)


#Convert a column into the correct datatype.
print("Convert a column into the correct datatype")
df["age"]=df["age"].astype(int)
print(df["age"].dtype)


#Drop unnecessary columns.
print("Drop unnecessary columns")

if "respondent_id" in df.columns:
    df = df.drop(columns=["respondent_id"])

print(df.columns)


#Save the cleaned dataset as a new CSV.

print("Save the cleaned dataset as a new CSV")
df.to_csv("cleaned_sleep_doomscrolling_habits.csv", index=False)
print("cleaned dataset saved successfully!")





#Data Exploration
print("\n.....................Data Exploration................\n")

#Count total unique values in every column.
print("Total unique values in every column")

for col in df.columns:
    print(col, ":", df[col].nunique())


#Display unique values of a selected column.
print("Unique values of a selected column")

print(df["gender"].unique())


#Find value counts of a categorical column.
print("Value counts of a categorical column")

for col in df.columns:
    print(df[col].value_counts())


#Find the most frequent value.
print("Most frequent value")
for col in df.columns:
    print(col, ":", df[col].mode()[0])


#Find the least frequent value.
print("Least frequent value")

for col in df.columns:
    counts=df[col].value_counts()
    print(col, ":", counts.index[-1])


#Find the maximum value.
print("The maximum value")
for col in df.select_dtypes(include="number").columns:
    print(col, ":", df[col].max())


#Find the minimum value.
print("The minimum value")
for col in df.select_dtypes(include="number").columns:
    print(col, ":", df[col].min())


#Find the average value.
print("The average value")
for col in df.select_dtypes(include="number").columns:
    print(col, ":", df[col].mean())


#Find the median value.
print("The median value")
for col in df.select_dtypes(include="number").columns:
    print(col, ":", df[col].median())


#Find the standard deviation value.
print("The standard deviation value")
for col in df.select_dtypes(include="number").columns:
    print(col, ":", df[col].std())    


#Find the Varience value.
print("The variance value")
for col in df.select_dtypes(include="number").columns:
    print(col, ":", df[col].var())


#Find the sum of a numerical column.
print("sum of a numerical column.")
for col in df.select_dtypes(include="number").columns:
    print(col, ":", df[col].sum())    




#Filtering
print("\n...............Filtering...........\n")  


#31. Display records where a numerical value is greater than a given threshold.
print("Numerical value is greater than a given threshold")

print(df[df["age"]>30])



#31. Display records where a numerical value is less than a given threshold.
print("Numerical value is less than a given threshold")

print(df[df["age"]<30])


#Filter using multiple conditions.
print("Filter using multiple conditions")
print(df[(df["age"]>30) & (df["stress_score"]>5)])



#Filter using OR conditions.
print(df[(df["age"]>30) | (df["stress_score"]>5)])



#Filter rows using .isin().
print("Rows using .isin()")

df=(df[df["gender"].isin(["Male","Female"])])

print(df[["age","gender"]])



#Filter rows using .between().
print("Rows using .between()")

df=(df[df["age"].between(22, 29)])
print(df["age"])



#Filter rows containing specific text.
print("Rows containing specific text")
df=df[df["gender"].str.contains("Male")]
print(df["gender"])