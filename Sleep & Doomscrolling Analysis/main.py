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

print("\nMissing values after filling with Mean:")
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

cleaned_file = os.path.join(current_folder, "cleaned_sleep_doomscrolling_habits.csv")
df.to_csv(cleaned_file, index=False)





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

df_is=(df[df["gender"].isin(["Male","Female"])])

print(df_is[["age","gender"]])



#Filter rows using .between().
print("Rows using .between()")

df_bet=(df[df["age"].between(22, 29)])
print(df_bet["age"])



#Filter rows containing specific text.
print("Rows containing specific text")
df_sp=df[df["gender"].str.contains("Male")]
print(df_sp["gender"])






print("\n................Sorting.............\n")
#Sort one column in ascending order.
print("Sorting one column in ascending order")
sort_df=df.sort_values(by="age", ascending=True)
print(sort_df)



#Sort one column in descending order.
print("Sorting one column in descending order")
sort_df=df.sort_values(by="age", ascending=False)
print(sort_df)


#Sort using multiple columns.
print("Sort using multiple columns")
sort_df=df.sort_values(by=["age","bedtime_screen_time_minutes"], ascending=[True, False])




#GroupBy Operations
print("\n..............GroupBy Operations............\n")

#Find the average of a numerical column grouped by a categorical column.
print("Average of a numerical column grouped by a categorical column")
average_sleep=df.groupby("gender")["sleep_hours_per_night"].mean()
print(average_sleep)



#Find the maximum value in each group.
print("Maximum value in each group")
max_value=df.groupby("gender")["age"].max()
print(max_value)



#Find the minimum value in each group.
print("minimum value in each group")
min_value=df.groupby("gender")["age"].min()
print(min_value)


#Count records in each group.
print("Records in each group")
count_record=df.groupby("gender").size()
print(count_record)



#Calculate the sum for each group.
print("Sum for each group")
sum_each=df.groupby("gender")["age"].sum()
print(sum_each)


#Indexing
print("\n...................Indexing................\n")
#Select specific rows using .loc.
print("Specific rows using .loc")
print(df.loc[0:4, ["age","gender"]])


#Select specific rows using .iloc.
print("Specific rows using .iloc")

#First row
print("First row")
print(df.iloc[0])

#Third row
print("Third row")
print(df.iloc[2])

#First Five Rows
print("First Five Row")
print(df.iloc[0:5])


#Rows 10 to 20
print("Rows 10 to 20")
print(df.iloc[10:21])


#Rows 0, 4 and 8
print("Rows0, 4, and 8")
print(df.iloc[[0, 4, 8]])


#First 3 rows and first 2 columns
print("First 3 rows and first 2 columns")
print(df.iloc[0:3, 0:2])


#Select specific columns.
print("Select specific columns")


#select one only column
print("select only one column")
print(["age"])


#select multiple column
print("Select multiple column")
print([["ID", "age", "gender"]])


#select first 3 column using iloc
print("Select first 3 column using iolc")
print(df.iloc[:, 0:3])


#select 2 column using loc
print("select 2 column using loc")
print(df.loc[:, ["age", "gender"]])




#String Operations
print("\n................String Operations............\n")

#Convert text to uppercase.
print("Convert text to uppercase")
df["gender"]=df["gender"].str.upper()
print(df["gender"])


#Convert text to lowercase.
print("Convert text to lowercase")
df["gender"]=df["gender"].str.lower()
print(df["gender"])



#Convert text to tilte case.
print("Convert text to tilte case")
df["gender"]=df["gender"].str.title()
print(df["gender"])



#Convert text to capitalize.
print("Convert text to capitalize")
df["gender"]=df["gender"].str.capitalize()
print(df["gender"])



#Remove extra spaces.
print("Remove extra spaces")
df["gender"]=df["gender"].str.strip()
print(df["gender"])


#Find rows containing a specific word.
print("Rows containing a specific world")
male_rows=df[df["gender"].str.contains("Male")]
print(male_rows)



#Replace text values.
print("Replace Male with M")
df["gender"]=df["gender"].replace("Male", "M")
print(df["gender"])
