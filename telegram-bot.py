import telegram

import os

import random

from time import sleep


filesindir = os.listdir("images")

while True:
    filename = random.choice(filesindir)
    file_path = os.path.join('images', filename)
    with open(file_path, 'rb') as photo:
        sleep(11440)