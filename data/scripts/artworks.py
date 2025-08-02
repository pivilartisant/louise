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


def entry_time_series_barplot(
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


def overlay_time_series_lineplot(
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
