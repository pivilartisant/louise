from data_class import ArtworkCols
from data_frames import artworks
import random

target = "Eugène Atget"
target_image_num = 5

# Utility Functions

def get_image_urls(artist:str)-> list:
    """Extracts image URLs from the artworks DataFrame """
    artworks_by_artists = artworks[artworks[ArtworkCols.Artist.value] == artist]

    return artworks_by_artists[ArtworkCols.ImageURL.value].dropna().to_list()

def get_random_image_urls(artworks_list:list[str], num_of_images:int) -> list[str]:
    """Downloads images for a given number of artworks randomly selecting in the """
    l = len(artworks_list)
    i = 0
    selected_images:list[str] = []
    while i <= num_of_images:
        # get target_image_num of image from a random selection of the artworks 
        selected_images.append(artworks_list[random.randrange(0, l)])
        i+=1
    if len(selected_images) == 0:
        print("ERROR NO IMAGE URL'S FOUND RETURNING EMPTY LIST")
        return selected_images
    
    return selected_images

target_image_urls = get_image_urls(target)

image_urls = get_random_image_urls(target_image_urls, target_image_num)

print(f"Selected {len(image_urls)}: {image_urls}")