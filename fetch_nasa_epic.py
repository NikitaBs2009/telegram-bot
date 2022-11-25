import os

from datetime import datetime

import requests

from pprint import pprint

from dotenv import load_dotenv

from main import download

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
    fetch_nasa_epic(api_key)