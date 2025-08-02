import re
import pandas as pd


def clean_years(items: pd.Series) -> pd.Series:
    """Normalizes years into a Series of integers with matching index"""
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
