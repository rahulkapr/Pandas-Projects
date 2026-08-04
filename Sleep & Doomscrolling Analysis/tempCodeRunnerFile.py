#Find the most frequent value.
print("Most frequent value")
for col in df.columns:
    print(col, ":", df[col].mode())