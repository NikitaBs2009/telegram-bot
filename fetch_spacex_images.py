import os

import requests

from main import download

from dotenv import load_dotenv

def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    image_links = response.json()["links"]["flickr"]["original"]
    for number, image_link in enumerate(image_links):
        file_path = f"images/{number} spacex.jpg"
        file_path = os.path.join('images', f"{number} spacex.jpg")
        download(image_link, file_path)
if __name__ == '__main__':
    load_dotenv()
    launch_id = os.getenv('5eb87d47ffd86e000604b38a')
    os.makedirs('images', exist_ok=True)
    fetch_spacex_last_launch()