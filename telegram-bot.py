import logging

import telegram

import os

import random

from time import sleep

from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    tg_chat_id = os.environ['TG_CHAT_ID']
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    filesindir = os.listdir("images")

    while True:
        try:
            filename = random.choice(filesindir)
            file_path = os.path.join('images', filename)
            with open(file_path, 'rb') as photo:
                bot.send_photo(tg_chat_id, photo=photo)
            sleep(11440)
        except telegram.error.NetworkError:
            logging.exception('разрыв соеденения')
            sleep(10)