import random
import subprocess
from data.scripts.artworks import ArtworkCols
from data_frames import artworks

# Utility Functions to Get Images

def get_image_url_by_artist(artist:str)-> list:
    """Extracts image URLs from the artworks DataFrame """
    artworks_by_artists = artworks[artworks[ArtworkCols.Artist.value] == artist]

    return artworks_by_artists[ArtworkCols.ImageURL.value].dropna().to_list()

def get_random_image_urls(artworks_list:list[str], num_of_images:int) -> list[str]:
    """Downloads a random images from artwork list"""
    l = len(artworks_list)
    i = 0
    selected_images:list[str] = []
    while i < num_of_images:
        # get target_image_num of image from a random selection of the artworks 
        selected_images.append(artworks_list[random.randrange(0, l)])
        i+=1
    if len(selected_images) == 0:
        print("ERROR NO IMAGE URL'S FOUND RETURNING EMPTY LIST")
        return selected_images
    
    return selected_images

def download_image(url:str, path:str):
    command = ["curl", url,"-o", "data/images/"+path+".jpg"]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    error = result.stderr
    if result.returncode != 0:
        print(f"Error downloading the image:{error}")