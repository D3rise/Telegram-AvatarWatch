## Инструкции по настройке аватарки-часов на своем аккаунте Telegram

1. Перейдите по этой [ссылке](https://my.telegram.org/) и войдите в свой аккаунт.
2. Установка зависимостей `pip3 install -r requirements.txt`   
3. Замените значения `api_id` и `api_hash` в файле .env.example  
4. Переименуйте файл `.env.example` в `.env`   
5. Сгенерируйте картинки с изображением времени: `python3 generate_time_images.py`
6. Запустите бота: `python3 main.py` 