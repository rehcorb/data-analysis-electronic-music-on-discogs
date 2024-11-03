import pandas as pd
import numpy as np

# 1. Load the CSV file
file_path = r"C:\Users\anais\OneDrive\Bureau\Formation Business Analyst - Adeline\Projet Github\discogs-data-electro-1990-2000\discogs_electronic.csv"
df = pd.read_csv(file_path, encoding='utf-8')

# 2. Promote headers (already done when loading with pd.read_csv)

# 3. Change column types
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

# 4. Replace missing values in 'country'
df['country'].replace('', 'Unknown', inplace=True)

# 5. Convert 'release_date' to date type
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# 6. Add the 'Year' column
df['Year'] = df['release_date'].dt.year

# 7. Reorder the columns
df = df[['artist', 'title', 'label', 'country', 'format', 'release_date', 'Year', 
         'genre', 'styles', 'have', 'want', 'num_ratings', 'average_rating', 
         'lowest_price', 'median_price', 'highest_price']]

# 8. Drop the 'release_date' column
df.drop(columns=['release_date'], inplace=True)

# 9. Rename 'Year' column to 'release_date'
df.rename(columns={'Year': 'release_date'}, inplace=True)

# 10. Replace dots with commas
for column in ['average_rating', 'lowest_price', 'median_price', 'highest_price']:
    df[column] = df[column].str.replace('.', ',', regex=False)

# 11. Remove dollar sign
for column in ['lowest_price', 'median_price', 'highest_price']:
    df[column] = df[column].str.replace('$', '', regex=False)

# 12. Change column types for prices and rating
df[['average_rating', 'lowest_price', 'median_price', 'highest_price']] = df[['average_rating', 'lowest_price', 'median_price', 'highest_price']].apply(pd.to_numeric, errors='coerce')

# 13. Replace error values with NaN
df[['average_rating', 'lowest_price', 'median_price', 'highest_price']] = df[['average_rating', 'lowest_price', 'median_price', 'highest_price']].fillna(np.nan)

# 14. Split the 'styles' column by the delimiter ','
styles_split = df['styles'].str.split(',', expand=True)
styles_split.columns = [f'styles.{i+1}' for i in range(styles_split.shape[1])]
df = pd.concat([df, styles_split], axis=1)

# Now df contains the processed data, and the styles column has been split
