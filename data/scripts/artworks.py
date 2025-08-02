import re
import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes
from enum import Enum
from typing import Optional


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


def clean_artwork_years(items: pd.Series) -> pd.Series:
    """Normalizes artwork years into a Series of integers with matching index"""
    cleaned_years = []

    for item in items:
        if isinstance(item, str):
            match = re.search(r"\b\d{4}\b", item)
            if match:
                cleaned_years.append(int(match.group()))
            else:
                cleaned_years.append(None)
        else:
            cleaned_years.append(None)

    return pd.Series(
        cleaned_years, index=items.index, dtype="Int64"
    )  # Nullable integer type


def artwork_per_year_histogram(
    year_counts: list[int],
    title: Optional[str] = None,
    ax: Axes = None,
) -> None:
    """Displays number of artworks created of the course of given year range"""
    value_counts = pd.Series(year_counts)
    df = pd.DataFrame({"Year": value_counts.index, "Count": value_counts.values})

    sns.barplot(data=df, x="Year", y="Count", ax=ax)
    ax.set_title(title)
    ax.tick_params(axis="x", rotation=90)


def created_acquired_year_scatter(
    created_series: list[int],
    aquired_series: list[int],
    title: Optional[str] = None,
    ax: Axes = None,
) -> None:
    created_df = pd.DataFrame(
        {"Year": created_series.index, "Count": created_series.values}
    )
    aquired_df = pd.DataFrame(
        {"Year": aquired_series.index, "Count": aquired_series.values}
    )
    sns.lineplot(
        x=created_df["Year"], y=created_df["Count"], color="forestgreen", ax=ax
    )
    sns.lineplot(x=aquired_df["Year"], y=aquired_df["Count"], color="pink", ax=ax)
    ax.set_title(title)
