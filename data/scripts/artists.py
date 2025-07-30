from enum import Enum
from artworks import ArtworkCols
from data_frames import artworks
import random

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
def get_most_represented_artist_in_classification(classification:str):
    # get all artworks in classification
    classified_artworks = artworks[artworks[ArtworkCols.Classification.value]==classification]
    # get all artists represented in classification
    artists_in_classification = classified_artworks[ArtworkCols.Artist.value]
    _artists_in_classification = artists_in_classification.loc[lambda x : (x != "Unknown artist") & (x != "Unidentified photographer")].value_counts()
    return _artists_in_classification.index[0]

# get least represented artist
def get_least_represented_artist_in_classification(classification:str):
    # get all artworks in classification
    classified_artworks = artworks[artworks[ArtworkCols.Classification.value]==classification]
    # get all artists represented in classification
    artists_in_classification = classified_artworks[ArtworkCols.Artist.value]
    _artists_in_classification = artists_in_classification.loc[lambda x : (x != "Unknown artist") & (x != "Unidentified photographer")].value_counts()
    return _artists_in_classification.index[len(_artists_in_classification)-1]





    # while i <= 5:
    #     r = random.randrange(0,len(eugene_atget_photographs))
    #     eugene_atget_random_selection.append(
    #         {
    #             ArtworkCols.Title.value:eugene_atget_photographs[ArtworkCols.Title.value].iloc[r],
    #             ArtworkCols.Date.value:eugene_atget_photographs[ArtworkCols.Date.value].iloc[r]
    #         }
    #     )
    #     i+=1

    # print(f"{Photographers.index[0]} {eugene_atget[ArtworkCols.ArtistBio.value].iloc[0]} is the most represented photographer with {Photographers.iloc[0]} photographs\n")
    # print(f"Some of his works include:\n")
    # for photograph in eugene_atget_random_selection:
    #     print(f"    {photograph[ArtworkCols.Title.value]} ({photograph[ArtworkCols.Date.value]})\n")