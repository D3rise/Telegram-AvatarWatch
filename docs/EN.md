## Instructions to set-up Telegram Avatar Watch

1. Go to this [link](https://my.telegram.org/) and login to your account.
2. Install dependancies `pip3 install -r requirements.txt`  
3. Replace values of `api_id` and `api_hash` in file .env.example  
4. Rename file `.env.example` into `.env`  
5. Generate images with time: `python3 generate_time_images.py`
6. Start the bot: `python3 main.py`