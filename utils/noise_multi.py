import numpy as np
import random


def add_noise_multi(image, noise_level): 
    sigma = noise_level
    row,col,ch = image.shape
    gauss = np.random.randn(row, col, ch)
    gauss = gauss.reshape(row, col, ch)        
    gauss = gauss * sigma
    noisy = image + image * gauss
    return noisy
    