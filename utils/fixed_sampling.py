import cv2


def img_fixed_sampling(img, target_size, method=None):
    if method is None:
        print("please specify the sampling type !!")
        exit()
    elif method == 'bicubic':
        return cv2.resize(img, (int(target_size[1]), int(target_size[0])), interpolation=cv2.INTER_CUBIC)
    elif method == 'bilinear':
        return cv2.resize(img, (int(target_size[1]), int(target_size[0])), interpolation=cv2.INTER_LINEAR)
    elif method == 'nearest':
        # nearest-neighbor interpolation introduces the misalignment issue
        return cv2.resize(img, (int(target_size[1]), int(target_size[0])), interpolation=cv2.INTER_NEAREST)
    elif method == 'area':
        return cv2.resize(img, (int(target_size[1]), int(target_size[0])), interpolation=cv2.INTER_AREA)
