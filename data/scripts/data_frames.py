import os
import pandas as pd

# Load data
artists_filepath = "Artists.csv"
artworks_filepath = "Artworks.csv"
raw_data_path = os.path.join("data", "raw")
artists = pd.read_csv(f"{raw_data_path}/{artists_filepath}")
artworks = pd.read_csv(f"{raw_data_path}/{artworks_filepath}")
