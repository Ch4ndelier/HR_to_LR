import numpy as np
import random
import cv2
from scipy import special
import torch
from torch.nn import functional as F
import torchvision.transforms as transforms


def filter2D(img, kernel):
    """PyTorch version of cv2.filter2D

    Args:
        img (Tensor): (b, c, h, w)
        kernel (Tensor): (b, k, k)
    """
    k = kernel.size(-1)
    b, c, h, w = img.size()
    if k % 2 == 1:
        img = F.pad(img, (k // 2, k // 2, k // 2, k // 2), mode='reflect')
    else:
        raise ValueError('Wrong kernel size')

    ph, pw = img.size()[-2:]

    if kernel.size(0) == 1:
        # apply the same kenrel to all batch images
        img = img.view(b * c, 1, ph, pw)
        kernel = kernel.view(1, 1, k, k)
        return F.conv2d(img, kernel, padding=0).view(b, c, h, w)
    else:
        img = img.view(1, b * c, ph, pw)
        kernel = kernel.view(b, 1, k, k).repeat(1, c, 1, 1).view(b * c, 1, k, k)
        return F.conv2d(img, kernel, groups=b * c).view(b, c, h, w)


def circular_lowpass_kernel(cutoff, kernel_size, pad_to=0):
    """2D sinc filter, ref: https://dsp.stackexchange.com/questions/58301/2-d-circularly-symmetric-low-pass-filter

    Args:
        cutoff (float): cutoff frequency in radians (pi is max)
        kernel_size (int): horizontal and vertical size, must be odd.
        pad_to (int): pad kernel size to desired size, must be odd or zero.
    """
    assert kernel_size % 2 == 1, 'Kernel size must be an odd number.'
    kernel = np.fromfunction(
        lambda x, y: cutoff * special.j1(cutoff * np.sqrt(
            (x - (kernel_size - 1) / 2)**2 + (y - (kernel_size - 1) / 2)**2)) / (2 * np.pi * np.sqrt(
                (x - (kernel_size - 1) / 2)**2 + (y - (kernel_size - 1) / 2)**2)), [kernel_size, kernel_size])
    kernel[(kernel_size - 1) // 2, (kernel_size - 1) // 2] = cutoff**2 / (4 * np.pi)
    kernel = kernel / np.sum(kernel)
    if pad_to > kernel_size:
        pad_size = (pad_to - kernel_size) // 2
        kernel = np.pad(kernel, ((pad_size, pad_size), (pad_size, pad_size)))
    return kernel


def tensor_to_np(tensor):
    tensor = tensor.clamp(0.0, 1.0)
    img = tensor.mul(255).byte()
    img = img.cpu().numpy().squeeze(0).transpose((1, 2, 0))
    return img


def sinc(img):
    kernel_range = [2 * v + 1 for v in range(3, 11)]
    kernel_size = random.choice(kernel_range)
    kernel_size = 21

    omega_c = np.random.uniform(np.pi / 3, np.pi)
    omega_c = np.pi / 3
    sinc_kernel = circular_lowpass_kernel(omega_c, kernel_size, pad_to=21)
    sinc_kernel = torch.FloatTensor(sinc_kernel)

    transf = transforms.ToTensor()
    img = transf(img)
    #print(img)
    img = img.unsqueeze(0)
    #print(img.shape)
    out = filter2D(img, sinc_kernel)
    #print("outshape:", out.shape)
    out = tensor_to_np(out)
    #print(out)
    return out