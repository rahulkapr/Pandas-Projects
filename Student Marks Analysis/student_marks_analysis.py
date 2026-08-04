import pandas as pd
import os

# Read the CSV file
current_folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(current_folder, "student_marks.csv")
df = pd.read_csv(csv_file)

print("Display the first 5 rows")
print(df.head())

print("Display the last 5 rows")
print(df.tail())

print("Dataset Information")
print(df.info())

print("Missing values")
print(df.isnull().sum())

print("Missing values fillup by using the median")
numerical_columns = df.select_dtypes(include="number").columns

for col in numerical_columns:
    df[col] = df[col].fillna(df[col].median())

print(df.isnull().sum())

print("Average marks in each subject:")
df["Average_Marks"] = df[["Math", "Science", "English"]].mean(axis=1)
print(df)

print("Topper")
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
topper = df.loc[df["Total"].idxmax()]
print(topper[["Student_ID", "Name", "Gender"]])

print("Students obtained above 80 marks in Math")
math_marksab = df[df["Math"] > 80]
print(math_marksab[["Student_ID", "Name", "Gender", "Math"]])

print("Students with attendance below 85")
Att_bl = df[df["Attendance"] < 85]
print(Att_bl[["Student_ID", "Name", "Gender", "Attendance"]])

print("Total Column")
print(df)

print("Percentage column")
df["Percentage"] = (df["Total"] / 300) * 100
print(df)

print("Assign Grade")

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    elif avg >= 50:
        return "E"
    else:
        return "F"

df["Grade"] = df["Average_Marks"].apply(grade)

print(df)

df = df.sort_values(by="Percentage", ascending=False)

print(df[["Name", "Percentage"]])

df.to_csv("cleaned_student_marks.csv", index=False)

print("Cleaned dataset saved successfully!")