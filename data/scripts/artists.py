from enum import Enum
from data.scripts.artworks import ArtworkCols
from data.scripts.utils.data_frames import artworks
import pandas as pd


class ArtistCols(Enum):
    ConstituentID = "ConstituentID"
    DisplayName = "DisplayName"
    ArtistBio = "ArtistBio"
    Nationality = "Nationality"
    Gender = "Gender"
    BeginDate = "BeginDate"
    EndDate = "EndDate"
    WikiQID = "Wiki QID"
    ULAN = "ULAN"


# get most represented artist
def get_most_represented_artist_in_classification(classification: str):
    # get all artworks in classification
    classified_artworks = artworks[
        artworks[ArtworkCols.Classification.value] == classification
    ]
    # get all artists represented in classification
    artists_in_classification = classified_artworks[ArtworkCols.Artist.value]
    _artists_in_classification = artists_in_classification.loc[
        lambda x: (x != "Unknown artist") & (x != "Unidentified photographer")
    ].value_counts()
    return _artists_in_classification.index[0]


# get least represented artist
def get_least_represented_artist_in_classification(classification: str):
    # get all artworks in classification
    classified_artworks = artworks[
        artworks[ArtworkCols.Classification.value] == classification
    ]
    # get all artists represented in classification
    artists_in_classification = classified_artworks[ArtworkCols.Artist.value]
    _artists_in_classification = artists_in_classification.loc[
        lambda x: (x != "Unknown artist") & (x != "Unidentified photographer")
    ].value_counts()
    return _artists_in_classification.index[len(_artists_in_classification) - 1]


def get_image_url_of_entries_by_artist(artist: str, df: pd.DataFrame) -> list[str]:
    """Returns image URLs for every entry for given artist in given DataFrame"""
    artworks_by_artists = df[df[ArtworkCols.Artist.value] == artist]
    return artworks_by_artists[ArtworkCols.ImageURL.value].dropna().to_list()
