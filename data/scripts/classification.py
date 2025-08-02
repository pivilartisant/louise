import random
from data.scripts.utils.data_frames import artworks
from data.scripts.artworks import ArtworkCols
from data.scripts.images.images import download_image
from typing import Optional
from matplotlib.axes import Axes
import seaborn as sns
from data.scripts.artists import (
    get_least_represented_artist_in_classification,
    get_most_represented_artist_in_classification,
)

classifications = artworks[ArtworkCols.Classification.value]

dir = "classification_examples"


def get_artwork_for_each_classification(classifications: list[str]) -> None:
    """This function iterates through each classification and download an image"""
    for classification in classifications:
        artwork_list = get_entry_image_urls_by_classification(classification)
        if artwork_list.empty:
            print(f"No artworks found for classification: {classification}")
            continue
        rand_in_list = artwork_list.iloc[random.randrange(0, len(artwork_list))]
        download_image(rand_in_list[ArtworkCols.ImageURL.value], dir, classification)


def get_entry_image_urls_by_classification(classification: str):
    """Extracts image URLs from the artworks DataFrame"""
    artworks_by_classification = artworks[
        artworks[ArtworkCols.Classification.value] == classification
    ]

    columns_to_keep = [
        ArtworkCols.Title.value,
        ArtworkCols.Artist.value,
        ArtworkCols.Date.value,
        ArtworkCols.ImageURL.value,
    ]
    # only drop without ImageURL
    artworks_by_classification_with_url = artworks_by_classification[
        columns_to_keep
    ].dropna(subset=[ArtworkCols.ImageURL.value])
    return artworks_by_classification_with_url


def classification_by_year_lineplot(
    df: list[int],
    cols: list[str],
    title: Optional[str] = None,
    ax: Axes = None,
) -> None:
    sns.lineplot(
        data=df[cols], palette=["pink", "blue", "purple", "green", "red"], ax=ax
    )
    ax.set_title(title)


def all_classification_by_year_lineplot(
    df: list[int],
    cols: list[str],
    title: Optional[str] = None,
    ax: Axes = None,
) -> None:
    palette = sns.color_palette("husl", n_colors=len(cols))
    sns.lineplot(
        data=df[cols], palette=palette, ax=ax
    )
    ax.legend(
        bbox_to_anchor=(0.5, -0.15),  # move below plot
        loc='upper center',
        ncol=4,                       
        fontsize=8,
        title='Classification',
        title_fontsize=10,
        frameon=False,
    )
    ax.grid(True)
    ax.set_title(title)



####### CLASSIFICATION DATA ANALYSIS
def get_most_and_least_represented_artist_in_each_classification():
    classifications_val_count = classifications.value_counts()

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
