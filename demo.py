import json
import cv2
from utils.apply import apply
with open("config/process.json") as f:
    process_dict = json.load(f)


x = cv2.imread('butterfly.png')


for progress, cfg in process_dict.items():
    print(key)
    print(cfg["pipline"])
    for method in cfg["pipline"]:
        print("using method " + method)
        x = apply(x, cfg, method)
    cv2.imwrite('demo_5.png', x)
    exit()
