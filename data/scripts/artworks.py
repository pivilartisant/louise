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

def clean_artwork_years(items:pd.Series)-> pd.Series:
    """normalizes artwork years into a list of ints"""
    years = []
    i=0
    while i < len(items):
        if not isinstance(items.iloc[i], str):
            i+=1
            continue
        
        match = re.search(r'\b\d{4}\b', items.iloc[i])
        if match:
            year = int(match.group())
            years.append(year)
            i+=1
        else:
            i+=1
            continue
    return pd.Series(years)

def display_artwork_per_year(cleaned_artwork_years: list[int], figsize=(10,8), title=None):
    """Displays number of artworks created of the course of given year range"""
    value_counts = pd.Series(cleaned_artwork_years)
    df = pd.DataFrame({'Year': value_counts.index, 'Count': value_counts.values})

    plt.figure(figsize=figsize)
    sns.barplot(x='Year', y='Count', data=df, color='steelblue')
    plt.xlabel('Artwork Creation Decade')
    plt.ylabel('Number of Artworks')
    plt.xticks(rotation=90)
    plt.title(title)
    plt.tight_layout()
    plt.show()