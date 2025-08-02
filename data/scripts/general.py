from artists import ArtistCols
from artworks import ArtworkCols
from utils.data_frames import artists, artworks
from utils.utils import clean_years

# Get general information on collection

artist_nationalities = artists[ArtistCols.Nationality.value].nunique()
departments = artworks[ArtworkCols.Department.value].nunique()
classifications = artworks[ArtworkCols.Classification.value].nunique()
mediums = artworks[ArtworkCols.Medium.value].nunique()

entries_created_at_year = (
    clean_years(artworks[ArtworkCols.Date.value]).dropna().sort_values()
)

entries_acquired_at_year = (
    artworks[ArtworkCols.DateAcquired.value].dropna().sort_values()
)

print("Information about the current MOMA collection:\n")
print(
    f"The MOMA counts {len(artworks)} artworks by {len(artists)} artists from {artist_nationalities} nationalities\n"
)
print(
    f"The MOMA currently counts {departments} departments with {classifications} different classifications and {mediums} mediums\n"
)

# Early and Latest Date Created
print(
    f"The earliest artwork dates back to: {entries_created_at_year.iloc[0]} and latest: {entries_created_at_year.iloc[len(entries_created_at_year) - 1]}\n"
)
# Early and Latest Date Acquired
print(
    f"The earliest acquired entry dates back to: {entries_acquired_at_year.iloc[0]} and latest: {entries_acquired_at_year.iloc[len(entries_acquired_at_year) - 1]}\n"
)
