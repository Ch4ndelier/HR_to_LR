import cv2


def go_jpeg(img, qua):
    #cv2.imwrite('temp.jpeg', img, [cv2.IMWRITE_JPEG_QUALITY, qua])
    #img = cv2.imread('temp.jpeg')
    jpeg_level = qua
    result, encimg = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_level])
    img = cv2.imdecode(encimg, 1)
    return img
