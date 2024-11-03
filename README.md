# Discogs Electronic Music Data Analysis (1990-2000)
**Project Overview**

This project focuses on performing detailed data analysis on electronic music records data from Discogs, covering the period from 1990 to 2000. The goal is to uncover trends, analyze artist popularity, genre distribution, 
and pricing patterns within the electronic music market. The dataset used for this analysis was sourced from Kaggle : 
https://www.kaggle.com/datasets/justinpakzad/discogs-electronic-music-dataset-1990-2000/data

I used Power BI and Power Query for data cleaning, transformation, and visualization, providing insights into the evolution of the electronic music scene during this decade.
I used Dax Studio for cleaned data exportation in csv format. 

**Dataset**

The dataset includes the following fields:

- artist: The name of the music artist or group.
- title: The title of the music track or album.
- label: The label that published the track.
- country: The country of origin of the release.
- format: The format of the release (e.g., vinyl, CD, etc.).
- release_date: The release date of the music.
- genre: The primary music genre (focus on electronic music).
- styles: More specific subgenres of the music.
- want: Number of people who have added the release to their wishlist.
- have: Number of people who own the release.
- num_ratings: The total number of user ratings for the release.
- average_rating: The average rating based on user input.
- lowest_price: The lowest recorded sale price of the release.
- median_price: The median price of the release.
- highest_price: The highest recorded sale price of the release.

**Project Structure**

- data:/: Contains the dataset, raw and cleaned. Data will be cleaned and transformed before use.
- notebooks/: Contains Jupyter notebooks used for preliminary exploration and analysis.
- results/: Visualizations, summary data, and other outputs from the analysis.
- README.md: This file, explaining the project and how to use it.

**How to Use**
- Clone the repository:
git clone https://github.com/rehcorb/data-analysis-electronic-music-on-discogs.git

- Load the Dataset:
Download the dataset from Kaggle and place it in the data/ directory, or use Power BI/Power Query to directly connect to the dataset.

- Run the Analysis:
Use Power BI to load and transform the dataset, perform data cleaning, and create visualizations.
Analyze key trends such as:
   - Most popular artists and styles.
   - Release formats by country.
   - Price trends over time.
   - The relationship between "wants," "haves," and pricing.
 
**Tools & Technologies**
- Power BI: For data visualization and reporting.
- Power Query: For data transformation and cleaning.
- Dax Studio: For cleaned data exportation in csv. 
- Python : For Jupyter notebooks.

**Data Transformation and Cleaning**
In Power Query, I performed several data transformations to prepare the dataset for analysis:

- Country: When the country field was empty, I assigned the value "Unknown" to maintain consistency across records.
- Release Date: I simplified the date information to the release year only, to streamline analysis.
- Price Fields (lowest_price, median_price, highest_price):
  - Replaced commas with periods to standardize decimal format.
  - Removed the $ sign to convert these fields to decimal format, making them suitable for numerical analysis.
- Ratings and Price Data:
  - If a record had no rating, I left it as null.
  - For records without any sales data or price information, I set these values to null as well.
After these transformations, I exported the cleaned dataset to CSV format using DAX Studio for further analysis.

**Analysis Goals**

Here are some of the key analyses we plan to perform:

- Genre and Subgenre Distribution: breakdown of the most common genres and subgenres in electronic music during 1990-2000.

- Artist Popularity: identify the most wanted and most owned releases and examine artist trends.

- Pricing Analysis: analyze pricing trends over time (lowest, median, and highest prices) ; correlate the number of ratings and average ratings with price evolution.

- Country of Origin: compare the distribution of electronic music releases by country and their associated pricing.

**Contributing**

Feel free to fork the project and submit pull requests if you'd like to contribute new analyses or improvements. Any suggestions to improve the analysis are welcome! :-)
