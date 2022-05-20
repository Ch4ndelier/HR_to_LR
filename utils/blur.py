import cv2
import random


def add_blur(img, cfg):
    k = 0
    if cfg["fix_kernel"]:
        k = 21
    else:
        k = random.randint(3, 10) * 2 + 1
    assert ("blur_sigma_up" in cfg) and ("blur_sigma_down" in cfg), "please specify blur sigma"
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
    # print("sigmaX", sigmaX)
    return cv2.GaussianBlur(img, (k, k), sigmaX)
