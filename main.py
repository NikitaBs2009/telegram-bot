import os

from urllib.parse import urlparse

from datetime import datetime

import requests

from pprint import pprint

from dotenv import load_dotenv

def get_extension(url):
    parsed_url = urlparse(url)
    return os.path.splitext(parsed_url.path)[1]


def download(url, file_path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ["API_KEY"]
    os.makedirs('images', exist_ok=True)
    fetch_nasa_epic(api_key)






