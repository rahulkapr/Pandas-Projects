import pandas as pd
import os

#Data Cleaning
print("\n............Data Cleaning...........\n")
#Check dataset shape
# Get the folder where main.py is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the CSV file
csv_file = os.path.join(current_folder, "netflix_titles.csv")

# Read the CSV file
df = pd.read_csv(csv_file)
print("Check dataset shape")
print(df.shape)


#Check data types
print("Check data types")
print(df.dtypes)


#Find missing values
print("Missing Values")
print(df.isnull().sum())


#Fill or remove missing values
print("Numeric columns with the median")
numeric_cols=df.select_dtypes(include="number").columns
df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols].median())



object_cols=df.select_dtypes(include="object").columns
for col in object_cols:
     if col != "duration":
        df[col]=df[col].fillna(df[col].mode()[0])

print(df.isnull().sum())    


#Remove duplicate records
print("Remove duplicate records")
print("Duplicate rows before removing:",df.duplicated().sum())

df=df.drop_duplicates()

print("Duplicate rows after removing:", df.duplicated().sum())


#Rename columns
print("Rename columns")
df.rename(columns={"listed_in": "genre"}, inplace=True)

print(df)
df["date_added"]=pd.to_datetime(df["date_added"], errors="coerce")

print(df["date_added"].dtype) 


#Save cleaned dataset
print("Saver cleaned dataset")
cleaned_file=os.path.join(current_folder, "cleaned_netflix_titles.csv")
df.to_csv(cleaned_file, index=False)

print("Cleaned dataset saved succeefully!")
print("File saved at:", cleaned_file)



#Content Overview
#Total titles
print("Total titles")
print(df["title"].count())
print(df["title"].nunique())

print("Total Movies: ",df[df["type"]=="Movie"].shape[0])
print("TV Show: ",df[df["type"]=="TV Show"].shape[0])


#Country Analysis
print("Country has produced the most netflix content")
print(df["country"].dropna().str.split(", ").explode().value_counts().head(10))



#Which type appears the most (Movie or TV Show)?
print("Type appears the most content")
type_count=df["type"].value_counts()

print("Most common type:", type_count.idxmax())
print("Number of titles:", type_count.max())

#What percentage of content is Movies vs TV Shows?
print("percentage of content is Movie or TV Show")

type_percet=((type_count/len(df))*100).round(2)
print(type_percet)



#Release Analysis
#Which year released the most content?
year_counts=df["release_year"].value_counts()
print("Year",year_counts.idxmax())
print("Content",year_counts.max())


#Top 10 countries
country_counts=df["country"].dropna().str.split(", ").explode().value_counts()
print(country_counts.head(10))


#Which countries produce mostly movies?
movies=df[df["type"]=="Movie"]
print(movies["country"].dropna().str.split(", ").explode().value_counts().head(1))




#Release Analysis
#Content growth over years
print("Content growth over years")
print(df["release_year"].value_counts().sort_index())

#Oldest content
print("Oldest Content")
print(df["release_year"].min())

#Newest content
print("Newest content")
print(df["release_year"].max())



#Ratings
#Most common rating
print("Most common rating")
print(df["rating"].value_counts().head(1))


#Least common rating
print("Least common rating")
print(df["rating"].value_counts().tail(1))


#Count of each rating
print("Count of each rating")
print(df["rating"].value_counts())



#Genres
#Most popular genre
print("Most popular genre")
mp=df["genre"].dropna().str.split(", ").explode().value_counts()
print(mp.head(1))

#Top 10 genres
print("Top 10 genres")
print(mp.head(10))


#Least common genres
print("Least common genres")
print(mp.tail(1))



#Directors
#Director with most titles
print("Director with most titles")
dmt=df["director"].value_counts()
print(dmt.head(1))

#Directors having multiple titles
print("Directors having multiple titles")
print(dmt[dmt>1])


#Duration
#Movies
movies=df[df["type"]=="Movie"]
movie_duration=(
    movies["duration"]
    .dropna()
    .str.replace("min", "", regex=False)
    .str.strip()
    .astype(int)
)
print("Longest Movie:", movie_duration.max(), "minutes")


print("Shortest Movie:",movie_duration.min(), "minutes")

print("Average duration:",movie_duration.mean().round(2), "minutes")


# TV Shows
TV = df[df["type"] == "TV Show"]

tv_seasons = (
    TV["duration"]
    .dropna()
    .str.extract(r"(\d+)")
    .astype(int)
)

print("Maximum Seasons:", tv_seasons.max().iloc[0])
print("Average Seasons:", round(tv_seasons.mean().iloc[0], 2))



#Monthly Trend
#Which month Netflix adds the most content?
print("Month Netflix adds the most content")
month_counts=df["date_added"].dt.month_name().value_counts()
print("Month with most content:", month_counts.idxmax())
print("Number of titles:",month_counts.max())

#Which year had the highest additions?
print("Year had the highest additions")
df["date_added"]=pd.to_datetime(df["date_added"])
year_counts=df["date_added"].dt.year.value_counts()
print("Year with most additions:",year_counts.idxmax())
print("Number of additions:",year_counts.max())