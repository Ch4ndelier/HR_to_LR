import cv2
import random


def add_blur(img, cfg):
    #k = random.randint(3, 10) * 2 + 1
    k = 21
    #TODO: k sigmaX 1to1
    #sigmaX = random.randint (24 / 10)
    sigmaX_up = cfg["blur_sigma_up"]
    sigmaX_down = cfg["blur_sigma_down"]
    if sigmaX_up == sigmaX_down:
        if sigmaX_up == 0:
            sigmaX = 0.01
        else:
            sigmaX = cfg["blur_sigma_up"]
    else:
        if sigmaX_down == 0:
            sigmaX_down = 0.01
        sigmaX = random.randint(int(sigmaX_down * 100), int(sigmaX_up * 100)) / 100
    print("X", sigmaX)
    return cv2.GaussianBlur(img, (k, k), sigmaX)
