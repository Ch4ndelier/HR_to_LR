import cv2
from PIL import Image


def go_jpeg(img, qua):
    cv2.imwrite('temp.png', img)
    img = Image.open('temp.png')
    img.save("temp.jpeg", quality=qua)
    img = cv2.imread('temp.jpeg')
    return img
