import pandas as pd

# Step 1: Load the CSV file
file_path = "C:/Users/anais/OneDrive/Bureau/Formation Business Analyst - Adeline/Projet Github/discogs-data-electro-1990-2000/discogs_electronic.csv"
df = pd.read_csv(file_path)

# Step 2: Promote headers (Pandas automatically uses the first row as header)
# No action needed here as pandas does this by default

# Step 3: Change data types
df = df.astype({
    "artist": str,
    "title": str,
    "label": str,
    "country": str,
    "format": str,
    "release_date": str,
    "genre": str,
    "styles": str,
    "have": 'Int64',
    "want": 'Int64',
    "num_ratings": 'Int64',
    "average_rating": str,
    "lowest_price": str,
    "median_price": str,
    "highest_price": str
})

# Step 4: Filter rows (keep all rows)
# This is redundant since we are keeping all rows

# Step 5: Replace empty strings with "Unknown" in the 'country' column
df['country'].replace("", "Unknown", inplace=True)

# Step 6: Change the 'release_date' column to datetime format
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Step 7: Insert 'Year' column from 'release_date'
df['Year'] = df['release_date'].dt.year

# Step 8: Reorder columns
df = df[["artist", "title", "label", "country", "format", "release_date", "Year",
         "genre", "styles", "have", "want", "num_ratings", "average_rating",
         "lowest_price", "median_price", "highest_price"]]

# Step 9: Drop the 'release_date' column
df.drop(columns=["release_date"], inplace=True)

# Step 10: Rename 'Year' column to 'release_date'
df.rename(columns={"Year": "release_date"}, inplace=True)

# Steps 11-14: Replace '.' with ',' in the specified columns
for column in ["average_rating", "lowest_price", "median_price", "highest_price"]:
    df[column] = df[column].str.replace('.', ',', regex=False)

# Steps 15-17: Remove '$' from the specified price columns
for column in ["lowest_price", "median_price", "highest_price"]:
    df[column] = df[column].str.replace('$', '', regex=False)

# Step 18: Change the data types for numerical columns
df = df.astype({
    "average_rating": float,
    "lowest_price": float,
    "median_price": float,
    "highest_price": float
})

# Step 19: Replace errors with nulls in specified columns
df['average_rating'].replace({pd.NA: None}, inplace=True)
df['lowest_price'].replace({pd.NA: None}, inplace=True)
df['median_price'].replace({pd.NA: None}, inplace=True)
df['highest_price'].replace({pd.NA: None}, inplace=True)

# Now df contains your transformed data
print(df.head())  # Display the first few rows of the DataFrame
