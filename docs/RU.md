## Инструкции по настройке аватарки-часов на своем аккаунте Telegram

1. Перейдите по этой [ссылке](https://my.telegram.org/) и войдите в свой аккаунт.  
2. Замените значения `api_id` и `api_hash` в файле config_example.py  
3. Переименуйте файл `config_example.py` в `config.py`  
4. Сгенерируйте картинки с изображением времени: `python3 generate_time_images.py`  
5. Запустите бота: `python3 main.py` 