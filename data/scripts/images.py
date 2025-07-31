# Utility Functions to Get Images
import random
import re
import subprocess

def get_random_image_urls(artworks_list: list[str], num_of_images: int) -> list[str]:
    """Downloads a random images from artwork list"""
    list_length = len(artworks_list)
    i = 0
    selected_images: list[str] = []
    while i < num_of_images:
        # get target_image_num of image from a random selection of the artworks
        selected_images.append(artworks_list[random.randrange(0, list_length)])
        i += 1
    if len(selected_images) == 0:
        print("ERROR NO IMAGE URL'S FOUND RETURNING EMPTY LIST")
        return selected_images

    return selected_images

def sanitize_path(path: str) -> str:
    """Converts to lowercase, removes special characters, replaces spaces with underscores"""
    path = path.lower()
    path = re.sub(r'[^\w\s-]', '', path)  # Remove special chars except alphanum, space, hyphen
    path = re.sub(r'\s+', '_', path)      # Replace spaces with underscores
    path = path.strip('_')                # Remove leading/trailing underscores
    return path


def download_image(url: str, dir:str, path: str):
    path = sanitize_path(path)
    command = ["curl", url, "-o", "data/images/" + dir + "/"+ path + ".jpg"]
    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    error = result.stderr
    if result.returncode != 0:
        print(f"Error downloading the image:{error}")
