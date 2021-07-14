import numpy as np
import random


def add_noise(img):
    row, col, ch = img.shape
    mean = 0
    sigma = random.randint(1, 5)
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy_img = img + gauss
    return noisy_img
