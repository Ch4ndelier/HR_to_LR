from utils.downsampling import img_downsampling
from utils.noise import add_noise
from utils.blur import add_blur
from utils.jpeg_encode import go_jpeg
from utils.patch_noise import add_patch_noise
from utils.sinc import sinc_filter
import random
import numpy as np


def apply(x, cfg, cfg_total, method):
    if method == 'downsample':
        return img_downsampling(x, scale=cfg['downsample_scale'], method=cfg['downsample_method'])
    elif method == 'blur':
        return add_blur(x, cfg)
    elif method == 'jpeg':
        q = random.randint(cfg['jpeg_quality_l'], cfg['jpeg_quality_h'])
        return go_jpeg(x, q)
    elif method == 'noise':
        if "noise_level" not in cfg_total:
            print("Please specify noise level")
            exit()
        return add_noise(x, cfg_total['noise_level'])
    elif method == 'sinc':
        if np.random.uniform() < cfg_total["sinc_prob"]:
            #print("sinc")
            return sinc_filter(x, cfg_total["sinc_lower_bound"], cfg_total["sinc_upper_bound"])
        else:
            return x
    elif method == 'patch_noise':
        return add_patch_noise(x)
    elif method == 'upsample':
        return img_downsampling(x, scale=cfg['upsample_scale'], method=cfg['upsample_method'])
    else:
        print("Undefined method")
        exit()
