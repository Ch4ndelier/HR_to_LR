import cv2


def img_downsampling(img, scale=0.5, method=None):
    assert method, "please specify the downsampling type !!"
    if method == 'bicubic':
        m, n = img.shape[0:2]
        return cv2.resize(img, (int(n * scale), int(m * scale)), interpolation=cv2.INTER_CUBIC)
    elif method == 'bilinear':
        m, n = img.shape[0:2]
        return cv2.resize(img, (int(n * scale), int(m * scale)), interpolation=cv2.INTER_LINEAR)
    elif method == 'nearest':
        m, n = img.shape[0:2]
        # nearest-neighbor interpolation introduces the misalignment issue
        return cv2.resize(img, (int(n * scale), int(m * scale)), interpolation=cv2.INTER_NEAREST)
    elif method == 'area':
        m, n = img.shape[0:2]
        return cv2.resize(img, (int(n * scale), int(m * scale)), interpolation=cv2.INTER_AREA)
