import cv2


def go_jpeg(img, qua):
    cv2.imwrite('temp.jpeg', img, [cv2.IMWRITE_JPEG_QUALITY, qua])
    img = cv2.imread('temp.jpeg')
    return img
