from data.scripts.classification import get_artwork_for_each_classification
from data.scripts.utils.data_frames import artworks
from data.scripts.artworks import ArtworkCols

# get example for each classification
classifications = artworks[ArtworkCols.Classification.value]
get_artwork_for_each_classification(classifications.unique())
