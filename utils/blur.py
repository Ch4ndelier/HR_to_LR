import cv2
import random


def add_blur(img):
    k = random.randint(3, 10) * 2 + 1
    sigmaX = random.randint(1, 24) / 10
    # print("X", sigmaX)
    return cv2.GaussianBlur(img, (k, k), sigmaX)
