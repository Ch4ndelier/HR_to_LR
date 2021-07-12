from utils.downsampling import img_downsampling
from utils.noise import add_noise
from utils.blur import add_blur
from utils.jpeg import go_jpeg
import random


def apply(x, cfg, method):
    if method == 'downsample':
        return img_downsampling(x, scale=cfg['downsample_scale'], method=cfg['downsample_method'])
    elif method == 'blur':
        return add_blur(x)
    elif method == 'jpeg':
        q = random.randint(cfg['jpeg_quality_l'], cfg['jpeg_quality_h'])
        return go_jpeg(x, q)
    elif method == 'noise':
        return add_noise(x)
    elif method == 'upsample':
        return img_downsampling(x, scale=cfg['upsample_scale'], method=cfg['upsample_method'])
    else:
        print("Undefined method")
        exit()
