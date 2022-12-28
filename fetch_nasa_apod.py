from main import download

import os

from dotenv import load_dotenv

import requests

from main import get_extension

def fetch_nasa_apod(api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': api_key,'count':30}
    response = requests.get(url, params=payload)
    response.raise_for_status()

    for number, image in enumerate(response.json()):
        if image['media_type'] == "image":
            link=image["hdurl"]
            file_path = os.path.join('images', f"{number}nasa{get_extension(link)}")
            download(link, file_path)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ["API_KEY"]
    os.makedirs('images', exist_ok=True)
    fetch_nasa_apod(api_key)