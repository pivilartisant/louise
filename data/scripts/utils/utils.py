import re
import pandas as pd


def clean_years(items: pd.Series) -> pd.Series:
    """Formats years"""
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


def clean_classification_dataframe(df: pd.DataFrame, df_date_col: str) -> pd.DataFrame:
    """Transforms long dataframe to wide dataframe. df: the dataframe you want to transform. df_date_col:the name of the column to be formated using clean_years()"""
    df = df.dropna(subset=[df_date_col]).copy()
    df[df_date_col] = clean_years(df[df_date_col])
    df = df.value_counts()
    df = df.reset_index(name="count")
    return df.pivot_table(
        index=df_date_col, columns="Classification", values="count", fill_value=0
    )


def get_most_in_dataframe(df: pd.DataFrame, head: int) -> list[any]:
    sum = df.sum(axis=0)

    return sum.sort_values(ascending=False).head(head).index.tolist()

def filter_by_amount(df:pd.DataFrame, n:int):
    s_total = df.sum(axis=0)

    # filtering out classifications with a minimum of n occurences
    f_series = s_total[
        s_total >= n
    ].index

    return df[f_series]
