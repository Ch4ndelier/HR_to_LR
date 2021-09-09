import cv2
import numpy as np
import random
# TODO: add edge blur

img = cv2.imread("/Users/liujunyuan/HR_to_LR/data/1k2kminus/0001.png")
# get edge
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge_output = cv2.Canny(gray_img, 0, 30)
print(edge_output.shape)
# get noise
row, col, ch = img.shape
mean = 0
sigma = random.randint(0, 5)
gauss = np.random.normal(mean, sigma, (row, col))
gauss = gauss.reshape(row, col)
print(gauss.shape)
# get masked_noise
masked_gauss = cv2.bitwise_and(gauss, gauss, mask=edge_output)
masked_gauss = np.expand_dims(masked_gauss, axis=2)
masked_gauss = np.repeat(masked_gauss, 3, axis=2)
#print(masked_gauss)
masked_img = np.clip(masked_gauss + img, 0, 255)

masked_img = masked_img.astype(np.uint8)
#print(img)
#print(masked_img)
#cv2.imshow("edge_output", masked_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite("/Users/liujunyuan/HR_to_LR/results/test/edgenoise.png", masked_img)
def add_edge_noise(img, noise_level):
    row, col, ch = img.shape
    mean = 0
    sigma = random.randint(0, noise_level)
    # print("noise_sigma", sigma)
    # sigma = 3
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy_img = img + gauss
    return noisy_img
