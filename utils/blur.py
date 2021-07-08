import cv2


def add_blur(img):
    return cv2.GaussianBlur(img, (7, 7), cv2.BORDER_DEFAULT)
