import matplotlib.pyplot as plt
from data_frames import artists, artworks
from artists import (
    ArtistCols,
    get_most_represented_artist_in_classification,
    get_least_represented_artist_in_classification,
)
from artworks import (
    ArtworkCols,
    clean_artwork_years,
    artwork_per_year_histogram,
    created_acquired_year_scatter,
)
from classification import plot_classification_per_year


fig, axs = plt.subplots(2, 2, figsize=(14, 6))
# Initializing Variables
artist_data_length = 0
artworks_data_length = 0

# Nationality
nunique_nationality = 0

# departments
departments_data_length = 0
most_represented_department = ""

# classification
classification_data_length = 0
most_represented_classification = 0

# medium
medium_data_length = 0
most_represented_medium = 0


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

departments_data_length = artworks[ArtworkCols.Department.value].nunique()
classifications = artworks[ArtworkCols.Classification.value]
classifications_val_count = classifications.loc[
    lambda x: (x != "Mies van der Rohe Archive")
    & (x != "Frank Lloyd Wright Archive")
    & (x != "Correspondence")
    & (x != "(not assigned)")
].value_counts()
classification_data_length = classifications.nunique()
medium_data_length = artworks[ArtworkCols.Medium.value].nunique()
artworks_data_length = len(artworks)
print("Information about the current MOMA collection:\n")
print(
    f"The MOMA counts {artworks_data_length} artworks by {artist_data_length} artists from {nunique_nationality} nationalities\n"
)
print(
    f"The MOMA currently counts {departments_data_length} departments with {classification_data_length} different classifications and {medium_data_length} mediums\n"
)


labels = [
    ArtworkCols.Department.value,
    ArtworkCols.Classification.value,
    ArtworkCols.Medium.value,
]

for label in labels:
    val_count = artworks[label].value_counts()
    most_represented_val = val_count.index[0]
    print(
        f"The most represented {label} is {most_represented_val} with {val_count.iloc[0]} entries\n"
    )

i = 0
while i < len(classifications_val_count):
    most_represented_artist = get_most_represented_artist_in_classification(
        classifications_val_count.index[i]
    )
    least_represented_artist = get_least_represented_artist_in_classification(
        classifications_val_count.index[i]
    )
    if (most_represented_artist) == least_represented_artist:
        print(
            f"{most_represented_artist} is the only artist in classification {classifications_val_count.index[i]}"
        )
        i += 1
        continue
    print(
        f"The most represented artist for {classifications_val_count.index[i]} is {most_represented_artist}"
    )
    print(
        f"The least represented artist for {classifications_val_count.index[i]} is {least_represented_artist}"
    )
    i += 1


# get data
raw_collection_year_range = artworks[ArtworkCols.Date.value]
raw_date_acquired_year_range = artworks[ArtworkCols.DateAcquired.value]
# clean years to YYYY format, drop empty and sort chronologically 
collection_year_range = clean_artwork_years(raw_collection_year_range).dropna().sort_values()
date_acquired_year_range = clean_artwork_years(raw_date_acquired_year_range).dropna().sort_values()


# gets count for entry and sort chronologically
sorted_collection_year_range = collection_year_range.value_counts().sort_index()
sorted_date_acquired_year_range = date_acquired_year_range.value_counts().sort_index()
# df_sorted_date_aquired_year_range = sorted_date_aquired_year_range.reset_index(name='count')
# print(df_sorted_date_aquired_year_range)
# group by decade 
sorted_collection_decade_range = sorted_collection_year_range.groupby(
    (sorted_collection_year_range.index // 10) * 10
).sum()

# each year
artwork_per_year_histogram(
    sorted_collection_decade_range, title="Created Entries per Decade", ax=axs[0, 0]
)
# group by decade
created_acquired_year_scatter(
    sorted_collection_year_range, sorted_date_acquired_year_range, title="Created Entries Per Year/Date Acquired", ax=axs[0, 1]
)
print(
    f"The earliest artwork dates back to: {collection_year_range.iloc[0]} and latest: {collection_year_range.iloc[len(collection_year_range) - 1]}"
)

# Plot number classification occurence per year

classification_and_year = artworks[[ArtworkCols.Classification.value, ArtworkCols.Date.value]].dropna()
classification_and_year[ArtworkCols.Date.value] = clean_artwork_years(classification_and_year[ArtworkCols.Date.value])
classification_and_year_freq = classification_and_year.value_counts()
# recast to dataframe for later operations

df_classification_and_year = classification_and_year_freq.reset_index(name="count")
classification_and_year_matrix = df_classification_and_year.pivot_table(index="Date", columns="Classification", values="count", fill_value=0)
plot_classification_per_year(classification_and_year_matrix,['Photograph','Print', 'Illustrated Book', 'Drawing', 'Design' ], title="Mapping of most represented classifications per year", ax=axs[1,0])
plot_classification_per_year(classification_and_year_matrix,['Media','Audio', 'Video', 'Multiple', 'Installation' ], title="Mapping of post-modernist classifications per year", ax=axs[1,1])

plt.tight_layout()
plt.show()
