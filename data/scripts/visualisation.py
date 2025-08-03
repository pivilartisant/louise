import pandas as pd
import matplotlib.pyplot as plt
from utils.data_frames import artworks
from utils.utils import (
    clean_years,
    clean_classification_dataframe,
    get_most_in_dataframe,
)

from artworks import (
    ArtworkCols,
    entry_time_series_barplot,
    overlay_time_series_lineplot,
)
from classification import (
    classification_by_year_lineplot, all_classification_by_year_lineplot
)

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


### Comparing date created versus date acquired time series

# Filtering out the Mies van der Rohe Archive & Frank Lloyd Wright Archive
valid_classifications = artworks[ArtworkCols.Classification.value].apply(
    lambda x: x not in ["Mies van der Rohe Archive", "Frank Lloyd Wright Archive"]
)
 #applying filter
filtered_artworks = artworks[valid_classifications]

# Classification by date created
classifications_by_date = filtered_artworks[
    [ArtworkCols.Classification.value, ArtworkCols.Date.value]
]

# classification by date acquired
classifications_by_date_acquired = filtered_artworks[
    [ArtworkCols.Classification.value, ArtworkCols.DateAcquired.value]
]

# clean each dataframe
classifications_by_date_matrix = clean_classification_dataframe(
    classifications_by_date, ArtworkCols.Date.value
)
classifications_by_date_acquired_matrix = clean_classification_dataframe(
    classifications_by_date_acquired,
    ArtworkCols.DateAcquired.value,
)


### Get top 5 classification by count value
head = 5

top5_classifications_by_date_created = get_most_in_dataframe(
    classifications_by_date_matrix, head
)
top5_classifications_by_date_acquired = get_most_in_dataframe(
    classifications_by_date_acquired_matrix, head
)

# Most represented classifications by year
classification_by_year_lineplot(
    classifications_by_date_matrix,
    top5_classifications_by_date_created,
    title="Most represented classifications by year",
    ax=axs[1, 0],
)

# Most represented classifications by date aquired
classification_by_year_lineplot(
    classifications_by_date_acquired_matrix,
    top5_classifications_by_date_acquired,
    title="Most represented classifications by date aquired",
    ax=axs[1, 1],
)

plt.tight_layout()
plt.show()
plt.close()

### Plot overall classification with 1000 entries

fig, axs = plt.subplots(2, 1, figsize=(14, 8))

classification_totals_by_creation_date = classifications_by_date_matrix.sum(axis=0)


# filtering out classifications with a minimum of 1000 occurences
relevant_classifications_by_creation_date = classification_totals_by_creation_date[
    classification_totals_by_creation_date >= 1000
].index
filtered_entries_classifications_by_date_matrix = (
    classifications_by_date_matrix[relevant_classifications_by_creation_date]
)

all_classification_by_year_lineplot(
    filtered_entries_classifications_by_date_matrix,
    filtered_entries_classifications_by_date_matrix.columns,
    title="Yearly Distribution of Artwork Classifications by Creation Date",
    ax=axs[0],
)

window = 3

# rolling average plot
all_classification_by_year_lineplot(
    filtered_entries_classifications_by_date_matrix.rolling(window=window).mean(),
    filtered_entries_classifications_by_date_matrix.columns,
    title=f"{window}-Year Rolling Average of Classifications by Creation Date",
    ax=axs[1],
)


plt.tight_layout()
plt.show()
plt.close()


### Ploto specific classification defined by art historical terms
fig, axs = plt.subplots(2, 2, figsize=(14, 6))

# todo: add modernist classification by year
# todo: add modernist classification by date acquired

classification_by_year_lineplot(
    classifications_by_date_matrix,
    ["Media", "Audio", "Video", "Multiple", "Installation"],
    title="Post-modernist classifications by Year",
    ax=axs[1, 0],
)
classification_by_year_lineplot(
    classifications_by_date_acquired_matrix,
    ["Media", "Audio", "Video", "Multiple", "Installation"],
    title="Post-modernist Classifications by Date Acquired",
    ax=axs[1, 1],
)
plt.tight_layout()
plt.show()
plt.close()
