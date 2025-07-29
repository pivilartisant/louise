import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from enum import Enum

class ArtworkCols(Enum):
    Title = "Title"
    Artist = "Artist"
    ConstituentID = "ConstituentID"
    ArtistBio = "ArtistBio"
    Nationality = "Nationality"
    BeginDate = "BeginDate"
    EndDate = "EndDate"
    Gender = "Gender"
    Date = "Date"
    Medium = "Medium"
    Dimensions = "Dimensions"
    CreditLine = "CreditLine"
    AccessionNumber = "AccessionNumber"
    Classification = "Classification"
    Department = "Department"
    DateAcquired = "DateAcquired"
    Cataloged = "Cataloged"
    ObjectID = "ObjectID"
    URL = "URL"
    ImageURL = "ImageURL"
    OnView = "OnView"
    Circumference = "Circumference (cm)"
    Depth = "Depth (cm)"
    Diameter = "Diameter (cm)"
    Height = "Height (cm)"
    Length = "Length (cm)"
    Weight = "Weight (kg)"
    Width = "Width (cm)"
    SeatHeight = "Seat Height (cm)"
    Duration = "Duration (sec.)"

def clean_artwork_years(items:list[str])-> list[int]:
    """normalizes artwork years into a list of ints"""
    years = []
    for item in items:
        if not isinstance(item, str):
            continue
        match = re.search(r'\b\d{4}\b', item)
        if match:
            year = int(match.group())
            years.append(year)
        else:
            continue
    return years

def display_artwork_per_year(cleaned_artwork_years: list[int], figsize=(10, 8), title=None):
    """Displays number of artworks created of the course of given year range"""
    value_counts = pd.Series(cleaned_artwork_years).value_counts().sort_index()
    df = pd.DataFrame({'Year': value_counts.index, 'Count': value_counts.values})

    plt.figure(figsize=figsize)
    sns.barplot(x='Year', y='Count', data=df, color='steelblue')
    plt.xlabel('Year')
    plt.ylabel('Number of Artworks')
    plt.xticks(rotation=45)
    plt.title(title)
    plt.tight_layout()
    plt.show()