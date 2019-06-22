from utils import *
import cv2
import numpy as np
from datetime import datetime, timedelta

start_time = datetime.strptime("2019-06-21", "%Y-%m-%d")  # Можете выбрать любую дату
end_time = start_time + timedelta(days=1)

def get_black_background():
    return np.zeros((500, 500))

def generate_image_with_text(text):
    image = get_black_background()
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(image, convert_time_to_string(start_time).replace(";", ":"), (int(image.shape[0]*0.134), int(image.shape[1]*0.57)), font, 4, (255, 0, 255), 2, cv2.LINE_AA)
    return image

while start_time < end_time:
    text = convert_time_to_string(start_time)
    image = generate_image_with_text(text)
    cv2.imwrite("time_images/%s.jpg" % text, image)
    start_time += timedelta(minutes=1)