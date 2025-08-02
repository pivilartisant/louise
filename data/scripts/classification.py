import random
from data_frames import artworks
from artworks import ArtworkCols
from images import download_image
from typing import Optional
from matplotlib.axes import Axes
import seaborn as sns

dir = "classification_examples"

def get_artwork_for_each_classification(classifications:list[str])-> None:
    """This function iterates through each classification and download an image"""
    for classification in classifications:
        artwork_list = get_image_url_by_classification(classification)
        if artwork_list.empty:
            print(f"No artworks found for classification: {classification}")
            continue
        rand_in_list = artwork_list.iloc[random.randrange(0, len(artwork_list))]
        download_image(rand_in_list[ArtworkCols.ImageURL.value], dir, classification)


def get_image_url_by_classification(classification: str):
    """Extracts image URLs from the artworks DataFrame"""
    artworks_by_classification = artworks[artworks[ArtworkCols.Classification.value] == classification]

    columns_to_keep = [ArtworkCols.Title.value, ArtworkCols.Artist.value, ArtworkCols.Date.value, ArtworkCols.ImageURL.value]
    # only drop without ImageURL
    artworks_by_classification_with_url = artworks_by_classification[columns_to_keep].dropna(subset=[ArtworkCols.ImageURL.value])
    return artworks_by_classification_with_url

def plot_classification_per_year(df: list[int],
    cols:list[str],
    title: Optional[str] = None,
    ax: Axes = None,
) -> None:
    sns.lineplot(data=df[cols], palette=['pink', 'blue', 'purple', 'green', 'red'], ax=ax)
    ax.set_title(title)
