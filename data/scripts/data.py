import re
import random
from data_class import ArtistCols, ArtworkCols
from data_frames import artists, artworks
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Initializing Variables
artist_data_length=0
artworks_data_length=0

# Nationality
nunique_nationality = 0

# departments
departments_data_length = 0
most_popular_department = ""

# classification
classification_data_length = 0
most_popular_classification = 0 

# medium 
medium_data_length = 0
most_popular_medium = 0 


# print(artists.head())
# print(artworks.head())

# Get basic data on artists
artist_data_length = len(artists)

# Get artist nationality
artist_nationalities = artists[ArtistCols.Nationality.value]

nunique_nationality = artist_nationalities.nunique()
# get single occurence of each artist nationality
# value_counts = artist_nationalities.value_counts()

# Get basic data on artworks
artworks_data_length = len(artworks)

categories_of_artworks = [ArtworkCols.Department.value, ArtworkCols.Classification.value, ArtworkCols.Medium.value]

departments_data_length=artworks[ArtworkCols.Department.value].nunique()
classification_data_length=artworks[ArtworkCols.Classification.value].nunique()
medium_data_length=artworks[ArtworkCols.Medium.value].nunique()
print("Information about the current MOMA collection:\n")
print(f"The MOMA counts {artworks_data_length} artworks by {artist_data_length} artists from {nunique_nationality} nationalities\n")
print(f"The MOMA currently counts {departments_data_length} departments with {classification_data_length} different classification and {medium_data_length} mediums\n")

for category in categories_of_artworks:
    category_data_length=artworks[category].nunique()
    category_val_count=artworks[category].value_counts()
    most_popular=category_val_count.index[0]
    print(f"The most popular {category} is {most_popular} with {category_val_count.iloc[0]} entries\n")

Photographs = artworks[artworks[ArtworkCols.Classification.value]=="Photograph"]
Photographers = Photographs[Photographs[ArtworkCols.Artist.value] != "Unidentified photographer"][ArtworkCols.Artist.value].value_counts()
eugene_atget = Photographs[Photographs[ArtworkCols.Artist.value] == "Eugène Atget"]

eugene_atget_photographs = eugene_atget[[ArtworkCols.Title.value, ArtworkCols.Date.value]]
eugene_atget_random_selection:list[dict] = []
i = 0
while i <= 5:
    r = random.randrange(0,len(eugene_atget_photographs))
    eugene_atget_random_selection.append(
        {
            ArtworkCols.Title.value:eugene_atget_photographs[ArtworkCols.Title.value].iloc[r],
            ArtworkCols.Date.value:eugene_atget_photographs[ArtworkCols.Date.value].iloc[r]
        }
    )
    i+=1
    
print(f"{Photographers.index[0]} {eugene_atget[ArtworkCols.ArtistBio.value].iloc[0]} is the most represented photographer with {Photographers.iloc[0]} photographs\n")
print(f"Some of his works include:\n")
for photograph in eugene_atget_random_selection:
    print(f"    {photograph[ArtworkCols.Title.value]} ({photograph[ArtworkCols.Date.value]})\n")

photograph_years = eugene_atget_photographs[ArtworkCols.Date.value]
print(f"num of years: {len(photograph_years)}")

def clean_artwork_years(items:list[str])-> list[int]:
    """normalizes artwork years into a list of ints"""
    years = []
    for item in items:
        if not isinstance(item, str):
            continue
        match = re.search(r'\b\d{4}\b', item)
        if match:
            year = int(match.group())
            years.append(year)
        else:
            continue
    return years

       
cleaned_artwork_years = clean_artwork_years(photograph_years)
def plot_val_counts(cleaned_artwork_years: list[int], figsize=(10, 8), title=None):
    value_counts = pd.Series(cleaned_artwork_years).value_counts().sort_index()
    df = pd.DataFrame({'Year': value_counts.index, 'Count': value_counts.values})

    plt.figure(figsize=figsize)
    sns.barplot(x='Year', y='Count', data=df, color='steelblue')
    plt.xlabel('Year')
    plt.ylabel('Number of Artworks')
    plt.xticks(rotation=45)
    plt.title(title)
    plt.tight_layout()
    plt.show()

plot_val_counts(cleaned_artwork_years, title='Number of Artworks produced by Eugene Atget')






