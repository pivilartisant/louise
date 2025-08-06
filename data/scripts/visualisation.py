import pandas as pd
import matplotlib.pyplot as plt
from utils.data_frames import artworks
from utils.utils import (
    clean_years,
    clean_classification_dataframe,
    get_most_in_dataframe,filter_by_amount
)

from artworks import (
    ArtworkCols,
    entry_time_series_barplot,
    overlay_time_series_lineplot,
)
from classification import (
    classification_by_year_lineplot, all_classification_by_year_heatmap, all_classification_by_year_stack, all_classification_by_year_lineplot
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


### Plot overall classification heatmap to get better understanding of classification creation

fig, ax = plt.subplots(1, 1, figsize=(14, 8))

# filtering out classifications with a minimum of 1000 occurences
filtered_classifications_by_date_acquired_matrix = filter_by_amount(classifications_by_date_acquired_matrix, 1000)
filtered_entries_classifications_by_date_matrix = filter_by_amount(classifications_by_date_matrix,1000)

all_classification_by_year_lineplot(
    filtered_entries_classifications_by_date_matrix,
    filtered_entries_classifications_by_date_matrix.columns,
    title="Yearly Distribution of Artwork Classifications by Creation Date",
    ax=ax,
)

plt.tight_layout()
plt.show()
plt.close()

fig, ax = plt.subplots(figsize=(14, 8))

classification_totals_by_creation_date = classifications_by_date_matrix.sum(axis=0)

# heatmap
all_classification_by_year_heatmap(classifications_by_date_matrix, "Classification heatmap, proportional to occurence count", ax=ax)

plt.tight_layout()
plt.show()
plt.close()


### Plot overall classification heatmap by date acquired to to get better understanding of museums aquirement trends
fig, axs = plt.subplots(3, 1, figsize=(14, 8))

rolling_window = 2

# stack area chart date acquired by year
all_classification_by_year_stack(filtered_classifications_by_date_acquired_matrix.rolling(window=rolling_window).mean(),"minmax","Classifications by Date Acquired Stacked Area Chart (MinMax)", ax=axs[0])
all_classification_by_year_stack(filtered_classifications_by_date_acquired_matrix.rolling(window=rolling_window).mean(),"mean","Classifications by Date Acquired Stacked Area Chart (Z-score)", ax=axs[1])
all_classification_by_year_stack(filtered_classifications_by_date_acquired_matrix.rolling(window=rolling_window).mean(),"proportional","Classifications by Date Acquired Stacked Area Chart (Proportional)",ax=axs[2])

plt.tight_layout()
plt.show()
plt.close()

# case study: "Cubism and Abstract Art”
# fig, axs = plt.subplots(2, 2, figsize=(14, 6))

# plt.tight_layout()
# plt.show()
# plt.close()


### case study "post modernist"
fig, axs = plt.subplots(2, 2, figsize=(14, 6))

# modernist_classifications = ["Painting", "Sculpture", "Architecture", "Photograph", "Collage", "Design" ]
post_modernist_classifications =  ["Media", "Audio", "Video", "Multiple", "Installation", "Digital", "Ephemera", "Performance"]

# classification_by_year_lineplot(
#     classifications_by_date_matrix,
#     modernist_classifications,
#     title="Modernist classifications by Year",
#     ax=axs[0, 0],
# )
# classification_by_year_lineplot(
#     classifications_by_date_acquired_matrix,
#     modernist_classifications,
#     title="Modernist Classifications by Date Acquired",
#     ax=axs[0, 1],
# )

classification_by_year_lineplot(
    classifications_by_date_matrix,
    post_modernist_classifications,
    title="Post-modernist classifications by Year",
    ax=axs[1, 0],
)
classification_by_year_lineplot(
    classifications_by_date_acquired_matrix,
    post_modernist_classifications,
    title="Post-modernist Classifications by Date Acquired",
    ax=axs[1, 1],
)
plt.tight_layout()
plt.show()
plt.close()
