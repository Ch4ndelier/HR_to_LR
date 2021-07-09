import json
import cv2
import random
from utils.load_data import get_img_list, load_config
from utils.process import process_single_image, get_process_list


config = load_config()
img_list = get_img_list(config["in_path"])
random.shuffle(img_list)
num_img = len(img_list)
process_list = get_process_list(config, num_img)

for img_info, p in zip(img_list, process_list):
    process_single_image(img_info, p)
