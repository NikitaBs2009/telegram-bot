# Загрузите в  телеграм фотографии космоса
Проект предназначен для скачивания фотографий с NASA, SPACEX, и отправки их в телеграм канал.
### Как установить
Ключ  NASA можно получить  на [сайте](https://api.nasa.gov/)  "APY_KEY"  он выглядет как огромный набор букв и цифр

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

Затем в  скрипте нужно создать файл `".env"` и записать в него токены. 
``` 
API_KEY=Ваш_ключ, 
LAUNCH_ID=Ваш_лаунч_айди, 
TG_TOKEN=Ваш_токен
 ```
### для использовния
Для скачивания фотографий  нужно ввести:
```
python fetch_nasa_apod.py
python fetch_nasa_epic.py
python fetch_spacex_images.py
```

Для отправки фото нужно ввести:
```
python telegram-bot.py
```
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).