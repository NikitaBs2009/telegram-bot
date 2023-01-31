import telegram

import os

import random

from time import sleep

from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    os.environ['TG_TOKEN']
    tg_token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=tg_token)
    filesindir = os.listdir("images")

    while True:
        filename = random.choice(filesindir)
        file_path = os.path.join('images', filename)
        with open(file_path, 'rb') as photo:
            bot.send_photo(chat_id, photo=photo)
            sleep(11440)


