import json
from utils.downsampling import img_downsampling
from utils.noise import add_noise
from utils.blur import add_blur
from utils.jpeg import go_jpeg
import cv2

with open("config/process.json") as f:
    process_dict = json.load(f)


x = cv2.imread('butterfly.png')


def apply(x, cfg, method):
    if method == 'downsample':
        return img_downsampling(x, scale=cfg['downsample_scale'], method=cfg['downsample_method'])
    elif method == 'blur':
        return add_blur(x)
    elif method == 'jpeg':
        return go_jpeg(x, qua=cfg['jpeg_quality'])
    elif method == 'noise':
        return add_noise(x)
    elif method == 'upsample':
        return img_downsampling(x, scale=cfg['upsample_scale'], method=cfg['upsample_method'])
    else:
        print("Undefined method")
        exit()


for key, cfg in process_dict.items():
    print(key)
    print(cfg)
    print(cfg["pipline"])
    for method in cfg["pipline"]:
        x = apply(x, cfg, method)
    cv2.imwrite('demo_2.png', x)
    exit()
