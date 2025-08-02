from classification import get_artwork_for_each_classification
from data_frames import artworks
from artworks import ArtworkCols

# get example for each classification
classifications = artworks[ArtworkCols.Classification.value]
get_artwork_for_each_classification(classifications.unique())
