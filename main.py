import os

from urllib.parse import urlparse

from datetime import datetime

import requests

from pprint import pprint

from dotenv import load_dotenv

def get_extension(url):
    parsed_url = urlparse(url)
    return os.path.splitext(parsed_url.path)[1]

def fetch_nasa_apod(api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': api_key,'count':30}
    response = requests.get(url, params=payload)
    response.raise_for_status()

    for number, image in enumerate(response.json()):
        if image['media_type'] == "image":
            link=image["hdurl"]
            file_path = f"./images/{number}nasa{get_extension(link)}"
            download(link, file_path)

def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    image_links = response.json()["links"]["flickr"]["original"]
    for number, image_link in enumerate(image_links):
        file_path = f"images/{number} spacex.jpg"
        download(image_link, file_path)

def download(url, file_path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)

def fetch_nasa_epic(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images/"
    payload = {'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pprint (response.json())
    for image in response.json():
        pprint(image["image"])
        pprint(image["date"])
        datetime_date = datetime.strptime(image["date"] , "%Y-%m-%d %H:%M:%S")
        format_date = (datetime_date.strftime('%Y/%m/%d'))
        image_path = f"./images/{image['image']}.png"
        image_link = f"https://api.nasa.gov/EPIC/archive/natural/{format_date}/png/{image['image']}.png"
        print (image_link)
        download(image_link, image_path, params=payload)
if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ["API_KEY"]
    os.makedirs('images', exist_ok=True)
    fetch_nasa_epic(api_key)






