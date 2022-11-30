import telegram

bot = telegram.Bot('5840879171:AAFjaF1LnoeCwkbDLw5yMTYyuOaiWl-Uttk')
print(bot.get_me())
with open('images/0nasa.jpg', 'rb') as photo:
    bot.send_photo(photo=photo, chat_id="-1001676726134")
