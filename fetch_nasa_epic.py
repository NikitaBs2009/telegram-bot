import os

from datetime import datetime

import requests

from pprint import pprint

from dotenv import load_dotenv

from tools import download

def fetch_nasa_epic(nasa_api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images/"
    payload = {'nasa_api_key': nasa_api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for image in response.json():
        datetime_date = datetime.strptime(image["date"] , "%Y-%m-%d %H:%M:%S")
        format_date = (datetime_date.strftime('%Y/%m/%d'))
        image_path = os.path.join('images',f"{image['image']}).png")
        image_link = f"https://api.nasa.gov/EPIC/archive/natural/{format_date}/png/{image['image']}.png"
        download(image_link, image_path, params=payload)
if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ["NASA_API_KEY"]
    os.makedirs('images', exist_ok=True)
    fetch_nasa_epic(nasa_api_key)