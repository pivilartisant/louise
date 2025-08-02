import matplotlib.pyplot as plt
from utils.data_frames import artworks
from utils.utils import clean_years

from artworks import (
    ArtworkCols,
    entry_time_series_barplot,
    overlay_time_series_lineplot,
)
from classification import classification_by_year_lineplot

# This script provides an overview of MOMA entries
# Note this queries the artworks which should be broadly considered as a "museum collection entry"

fig, axs = plt.subplots(2, 2, figsize=(14, 6))

# get data
entries_created_by_year = artworks[ArtworkCols.Date.value]
entries_acquired_by_year = artworks[ArtworkCols.DateAcquired.value]

# clean years to YYYY format, drop empty and sort chronologically
entries_created_by_year = (
    clean_years(entries_created_by_year).dropna().value_counts().sort_index()
)
entries_acquired_by_year = (
    clean_years(entries_acquired_by_year).dropna().value_counts().sort_index()
)

# group by decade
entries_created_by_decade = entries_created_by_year.groupby(
    (entries_created_by_year.index // 10) * 10
).sum()

# each year
entry_time_series_barplot(
    entries_created_by_decade, title="Entries Created by Decade", ax=axs[0, 0]
)
# group by decade
overlay_time_series_lineplot(
    entries_created_by_year,
    entries_acquired_by_year,
    title="Overlayed Created and Acquired by Year",
    ax=axs[0, 1],
)

# Plot number classification occurence per year
entries_classifications_by_date = artworks[
    [ArtworkCols.Classification.value, ArtworkCols.Date.value]
].dropna()

entries_classifications_by_date[ArtworkCols.Date.value] = clean_years(
    entries_classifications_by_date[ArtworkCols.Date.value]
)

entries_classifications_by_date_freq = entries_classifications_by_date.value_counts()
# recast to dataframe for later operations

entries_classifications_by_date = entries_classifications_by_date_freq.reset_index(
    name="count"
)
entries_classifications_by_date_matrix = entries_classifications_by_date.pivot_table(
    index="Date", columns="Classification", values="count", fill_value=0
)
classification_by_year_lineplot(
    entries_classifications_by_date_matrix,
    ["Photograph", "Print", "Illustrated Book", "Drawing", "Design"],
    title="Most represented classifications by year",
    ax=axs[1, 0],
)

# Plot number classification occurence per year
entries_classifications_by_date = artworks[
    [ArtworkCols.Classification.value, ArtworkCols.DateAcquired.value]
].dropna()

entries_classifications_by_date[ArtworkCols.DateAcquired.value] = clean_years(
    entries_classifications_by_date[ArtworkCols.DateAcquired.value]
)

entries_classifications_by_date_freq = entries_classifications_by_date.value_counts()
# recast to dataframe for later operations

entries_classifications_by_date = entries_classifications_by_date_freq.reset_index(
    name="count"
)
entries_classifications_by_date_matrix = entries_classifications_by_date.pivot_table(
    index="DateAcquired", columns="Classification", values="count", fill_value=0
)
classification_by_year_lineplot(
    entries_classifications_by_date_matrix,
    ["Photograph", "Print", "Illustrated Book", "Drawing", "Design"],
    title="Most represented classifications by date aquired",
    ax=axs[1, 1],
)
# todo add date acquired classifications 

plt.tight_layout()
plt.show()
plt.close()
fig, axs = plt.subplots(2, 2, figsize=(14, 6))

# todo: add modernist classification by year 
classification_by_year_lineplot(
    entries_classifications_by_date_matrix,
    ["Media", "Audio", "Video", "Multiple", "Installation"],
    title="Post-modernist classifications by year",
    ax=axs[1, 1],
)
plt.tight_layout()
plt.show()
plt.close()