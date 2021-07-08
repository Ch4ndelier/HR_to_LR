import cv2
import numpy as np
from utils.downsampling import img_downsampling
from utils.noise import add_noise
from utils.blur import add_blur
from utils.jpeg import go_jpeg
import json


x = cv2.imread('/Users/liujunyuan/HR_to_LR/butterfly.png')
x = go_jpeg(x)

print(img_downsampling(x, scale=2, method="nearest").shape)
x = img_downsampling(x, scale=0.5, method="nearest")
print(add_noise(x).shape)
x = add_noise(x)
x = add_blur(x)
x = img_downsampling(x, scale=2, method="nearest")
cv2.imwrite('testpipline.png', x)