import cv2
import random


def add_blur(img):
    k = random.randint(3, 10) * 2 + 1
    #TODO: k sigmaX 1to1
    #sigmaX = random.randint (24 / 10)
    sigmaX = 2.4
    # print("X", sigmaX)
    return cv2.GaussianBlur(img, (k, k), sigmaX)
