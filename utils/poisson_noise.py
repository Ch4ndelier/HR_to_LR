import numpy as np


def generate_poisson_noise(img, scale):
    """Generate poisson noise.
    Ref: https://github.com/scikit-image/scikit-image/blob/main/skimage/util/noise.py#L37-L219
    Args:
        img (Numpy array): Input image, shape (h, w, c), range [0, 1], float32.
        scale (float): Noise scale. Default: 1.0.
        gray_noise (bool): Whether generate gray noise. Default: False.
    Returns:
        (Numpy array): Returned noisy image, shape (h, w, c), range[0, 1],
            float32.
    """
    # round and clip image for counting vals correctly
    img = np.clip((img * 255.0).round(), 0, 255) / 255.
    vals = len(np.unique(img))
    vals = 2**np.ceil(np.log2(vals))
    out = np.float32(np.random.poisson(img * vals) / float(vals))
    noise = out - img
    return noise * scale


def add_poisson_noise(img, scale):
    noise = generate_poisson_noise(img/255, scale)
    out = img/255 + noise
    return out * 255
