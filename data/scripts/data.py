import os
import pandas as pd
import random
import matplotlib.pyplot as plt
from data_class import ArtistCols, ArtworkCols

# Load data
artists_filepath = "Artists.csv"
artworks_filepath = "Artworks.csv"
raw_data_path = os.path.join("data","raw")
artists = pd.read_csv(f"{raw_data_path}/{artists_filepath}")
artworks = pd.read_csv(f"{raw_data_path}/{artworks_filepath}")


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
print(f"{Photographers.index[0]} {eugene_atget[ArtworkCols.ArtistBio.value].iloc[0]} is the most represented photographer with {Photographers.iloc[0]} photographs\n")
eugene_atget_photographs = eugene_atget[[ArtworkCols.Title.value, ArtworkCols.Date.value]]
eugene_atget_random_selection:list[dict] = []
i = 0
while i <= 5:
    r = random.randrange(0,len(eugene_atget_photographs))
    eugene_atget_random_selection.append(
        {
            "title":eugene_atget_photographs[ArtworkCols.Title.value].iloc[r],
            "date":eugene_atget_photographs[ArtworkCols.Date.value].iloc[r]
        }
    )
    i+=1
print(f"Some of his works include:\n")
for photograph in eugene_atget_random_selection:
    print(f"    {photograph['title']} ({photograph['date']})\n")









