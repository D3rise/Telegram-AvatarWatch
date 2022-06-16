import os

from telethon import TelegramClient, sync
from dotenv import load_dotenv

from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
from utils import *

load_dotenv()

client = TelegramClient("timeavatar", os.getenv('api_id'), os.getenv('api_hash'))
client.start()

prev_update_time = ""

def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != prev_time

while True:
    if time_has_changed(prev_update_time):
        prev_update_time = convert_time_to_string(datetime.now())
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f"time_images/{prev_update_time}.jpg")
        client(UploadProfilePhotoRequest(file))
        print(f'Change avatar to {prev_update_time.replace(";", ":")}')