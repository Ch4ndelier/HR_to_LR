from utils.downsampling import img_downsampling
from utils.noise import add_noise
from utils.poisson_noise import add_poisson_noise
from utils.blur import add_blur
from utils.jpeg_encode import go_jpeg
from utils.noise_multi import add_noise_multi
from utils.patch_noise import add_patch_noise
from utils.sinc import sinc_filter
from utils.rotate import go_rotate
from utils.fixed_sampling import img_fixed_sampling
import random
import numpy as np


ori_scale = None


def apply(x, cfg, cfg_total, method):
    global ori_scale
    if method == 'downsample':
        if cfg_total["is_random_dropout"]:
            return img_downsampling(x, scale=cfg['downsample_scale'], method=random.choice(cfg['downsample_method_list']))
        else:
            return img_downsampling(x, scale=cfg['downsample_scale'], method=cfg['downsample_method'])
    elif method == 'blur':
        return add_blur(x, cfg)
    elif method == 'jpeg':
        q = random.randint(cfg['jpeg_quality_l'], cfg['jpeg_quality_h'])
        return go_jpeg(x, q)
    elif method == 'rotate':
        angle = random.randint(cfg['rot_angle_min'], cfg['rot_angle_max'])
        return go_rotate(x, angle)
    elif method == 'noise':
        if "noise_level" not in cfg_total:
            print("Please specify noise level")
            exit()
        p = random.randint(0, 1)
        if p:
            return add_noise(x, cfg_total['noise_level'])
        else:
            scale = random.randint(5, cfg_total['poisson_level']) / 100
            return add_poisson_noise(x, scale)
    elif method == 'sinc':
        if np.random.uniform() < cfg_total["sinc_prob"]:
            #print("sinc")
            if "sinc_lower_bound" not in cfg_total or "sinc_upper_bound" not in cfg_total:
                return sinc_filter(x)
            else:
                return sinc_filter(x, cfg_total["sinc_lower_bound"], cfg_total["sinc_upper_bound"])
        else:
            return x
    elif method == 'patch_noise':
        return add_patch_noise(x)
    elif method == 'noise_multi':
        return add_noise_multi(x)
    elif method == 'upsample':
        return img_downsampling(x, scale=cfg['upsample_scale'], method=cfg['upsample_method'])
    elif method == 'fixed_downsample':
        h, w, c = x.shape
        ori_scale = (h, w)
        down_scale_upper_bound = cfg['fixed_downsample_scale_upper_bound']
        down_scale_lower_bound = cfg['fixed_downsample_scale_lower_bound']
        assert down_scale_upper_bound >= down_scale_lower_bound, "upper bound is lower than lower bound"
        if down_scale_upper_bound == down_scale_lower_bound:
            down_scale = down_scale_upper_bound
        else:
            down_scale = random.randint(int(down_scale_lower_bound * 20), int(down_scale_upper_bound * 20)) / 20
        # precision: 0.05
        #down_scale = cfg['fixed_downsample_scale']
        target_size = (h * down_scale, w * down_scale)
        if cfg_total['is_random'] or cfg_total['is_random_dropout']:
            return img_fixed_sampling(x, target_size, method=random.choice(cfg['downsample_method_list']))
        else:
            return img_fixed_sampling(x, target_size, method=cfg['downsample_method'])
    elif method == 'fixed_upsample':
        out_scale = cfg['out_scale']
        assert ori_scale, "upsample before downsample!!"
        target_size = (ori_scale[0] * out_scale, ori_scale[1] * out_scale)
        if cfg_total['is_random'] or cfg_total['is_random_dropout']:
            return img_fixed_sampling(x, target_size, method=random.choice(cfg['downsample_method_list']))
        else:
            return img_fixed_sampling(x, target_size, method=cfg['upsample_method'])
    else:
        assert False, "Undefined method!"
