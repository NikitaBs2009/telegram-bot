import os

import requests
from dotenv import load_dotenv

from tools import download


def fetch_spacex_last_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    image_links = response.json()["links"]["flickr"]["original"]
    for number, image_link in enumerate(image_links):
        file_path = os.path.join("images", f"{number} spacex.jpg")
        download(image_link, file_path)


if __name__ == '__main__':
    load_dotenv()
    launch_id = os.getenv('LAUNCH_ID', '5eb87d47ffd86e000604b38a')
    os.makedirs('images', exist_ok=True)
    fetch_spacex_last_launch(launch_id)
