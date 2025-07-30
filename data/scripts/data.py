import random
from data_frames import artists, artworks
from artists import ArtistCols, get_most_popular_artist_in_classification, get_least_popular_artist_in_classification
from artworks import ArtworkCols



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
# Get basic data on the museum

departments_data_length=artworks[ArtworkCols.Department.value].nunique()
classifications = artworks[ArtworkCols.Classification.value]
classifications_val_count = classifications.loc[lambda x : (x != "Mies van der Rohe Archive") & (x != "Frank Lloyd Wright Archive") & (x != "Correspondence") & (x != "(not assigned)")].value_counts()
classification_data_length= classifications.nunique()
medium_data_length=artworks[ArtworkCols.Medium.value].nunique()
artworks_data_length = len(artworks)
print("Information about the current MOMA collection:\n")
print(f"The MOMA counts {artworks_data_length} artworks by {artist_data_length} artists from {nunique_nationality} nationalities\n")
print(f"The MOMA currently counts {departments_data_length} departments with {classification_data_length} different classifications and {medium_data_length} mediums\n")


labels = [ArtworkCols.Department.value, ArtworkCols.Classification.value, ArtworkCols.Medium.value]

for label in labels:
    val_count=artworks[label].value_counts()
    most_popular_val=val_count.index[0]
    print(f"The most popular {label} is {most_popular_val} with {val_count.iloc[0]} entries\n")

i = 0
while i < len(classifications_val_count):
    most_popular_artist = get_most_popular_artist_in_classification(classifications_val_count.index[i])
    least_popular_artist = get_least_popular_artist_in_classification(classifications_val_count.index[i])
    if (most_popular_artist) == least_popular_artist:
            print(f"{most_popular_artist} is the only artist in classification {classifications_val_count.index[i]}")
            i+=1
            continue
    print(f"The most popular artist for {classifications_val_count.index[i]} is {most_popular_artist}")
    print(f"The least popular artist for {classifications_val_count.index[i]} is {least_popular_artist}")
    i+=1








