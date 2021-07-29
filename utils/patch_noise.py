import numpy as np
import random
import torch
from PIL import Image
import os
import cv2
import math

noise_dir = '/Users/liujunyuan/HR_to_LR/TCLnoise'


def add_patch_noise(img):
    row, col, ch = img.shape
    # print(row, col, ch)
    # get source image
    source_image = np.array(img.transpose(2, 0, 1))
    t_source_image = torch.from_numpy(source_image).type(torch.Tensor)
    # print("ts", t_source_image.size())

    # get noise image
    files = os.listdir(noise_dir)
    n = len(files)
    ind = np.random.randint(0, n)
    img_dir = os.path.join(noise_dir, files[ind])
    image = cv2.imread(img_dir)

    # print(image)
    noise_image = np.array(image.transpose(2, 0, 1))
    t_noise_image = torch.from_numpy(noise_image).type(torch.Tensor)
    # print("tn", t_noise_image.size())

    # get noise
    norm_noise = (t_noise_image - torch.mean(t_noise_image, dim=[1, 2], keepdim=True))
    # print(norm_noise)
    # print("tn_n", norm_noise.size())

    m = math.ceil(t_source_image.size(1) / t_noise_image.size(1))
    n = math.ceil(t_source_image.size(2) / t_noise_image.size(2))
    # print("MN", m, n)
    # print(norm_noise.repeat(1, m, n).shape)
    norm_noise = norm_noise.repeat(1, m, n)
    t_source_image = t_source_image + norm_noise[:, 0:int(t_source_image.size(1)), 0:int(t_source_image.size(2))]
    t_source_image = torch.clamp(t_source_image, 0, 255)
    # print(t_source_image.size())
    return t_source_image.numpy().transpose(1, 2, 0)
