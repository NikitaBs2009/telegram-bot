from main import download

import os

from dotenv import load_dotenv

import requests

from main import get_extension

def fetch_nasa_apod(nasa_api_key,count):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'nasa_api_key': nasa_api_key,'count':count}
    response = requests.get(url, params=payload)
    response.raise_for_status()

    for number, image in enumerate(response.json()):
        if image['media_type'] == "image":
            link=image["hdurl"]
            file_path = os.path.join('images', f"{number}nasa{get_extension(link)}")
            download(link, file_path)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ["NASA_API_KEY"]
    photo_quantity = os.getenv("FOTO_QUANTITY",30)
    os.makedirs('images', exist_ok=True)
    fetch_nasa_apod(nasa_api_key)
