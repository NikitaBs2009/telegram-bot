import os

from urllib.parse import urlparse

import requests


def get_extension(url):
    parsed_url = urlparse(url)
    return os.path.splitext(parsed_url.path)[1]


def download(url, file_path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
