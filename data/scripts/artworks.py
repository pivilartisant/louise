import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
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

def artwork_per_year_histogram(list: list[int], title=None, ax:Axes=None):
    """Displays number of artworks created of the course of given year range"""
    value_counts = pd.Series(list)
    df = pd.DataFrame({'Year': value_counts.index, 'Count': value_counts.values})


    sns.barplot(data=df, x='Year', y='Count', ax=ax)
    ax.set_title(title)
    ax.tick_params(axis='x', rotation=90)

def artworks_per_year_scatter(list: list[int], title=None,ax:Axes=None):
    value_counts = pd.Series(list)
    df = pd.DataFrame({'Year': value_counts.index, 'Count': value_counts.values})
    sns.scatterplot(x=df['Year'], y=df['Count'], color='steelblue')
    ax.set_title(title)
