# Discogs Electronic Music Data Analysis (1990-2000)
**Project Overview**

This project focuses on performing detailed data analysis on electronic music data from Discogs, covering the period from 1990 to 2000. The goal is to uncover trends, analyze artist popularity, genre distribution, 
and pricing patterns within the electronic music market. The dataset used for this analysis was sourced from Kaggle : 
https://www.kaggle.com/datasets/justinpakzad/discogs-electronic-music-dataset-1990-2000/data

We will utilize Power BI and Power Query for data cleaning, transformation, and visualization, providing insights into the evolution of the electronic music scene during this decade.

**Dataset**

The dataset includes the following fields:

- Artist: The name of the music artist or group.
- Title: The title of the music track or album.
- Label: The label that published the track.
- Country: The country of origin of the release.
- Format: The format of the release (e.g., vinyl, CD, etc.).
- Date: The release date of the music.
- Genre: The primary music genre (focus on electronic music).
- Subgenre: More specific subgenres of the music.
- Want Count: Number of people who have added the release to their wishlist.
- Have Count: Number of people who own the release.
- Number of Ratings: The total number of user ratings for the release.
- Average Rating: The average rating based on user input.
- Lowest Price: The lowest recorded sale price of the release.
- Median Price: The median price of the release.
- Highest Price: The highest recorded sale price of the release.

**Project Structure**

- data/: Contains the dataset. Data will be cleaned and transformed before use.
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
   - Most popular artists and genres.
   - Release formats by country.
   - Price trends over time.
   - The relationship between "wants," "haves," and pricing.
 
**Tools & Technologies**
- Power BI: For data visualization and reporting.
- Power Query: For data transformation and cleaning.

**Analysis Goals**

Here are some of the key analyses we plan to perform:

- Genre and Subgenre Distribution: breakdown of the most common genres and subgenres in electronic music during 1990-2000.

- Artist Popularity: identify the most wanted and most owned releases and examine artist trends.

- Pricing Analysis: analyze pricing trends over time (lowest, median, and highest prices) ; correlate the number of ratings and average ratings with price evolution.

- Country of Origin: compare the distribution of electronic music releases by country and their associated pricing.

**Contributing**

Feel free to fork the project and submit pull requests if you'd like to contribute new analyses or improvements. Any suggestions to improve the analysis are welcome! :-)
