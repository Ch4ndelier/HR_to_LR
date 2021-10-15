import cv2
import numpy as np
import torchvision.transforms.functional as F
import torch


def go_rotate(image, angle):
    h, w, c = image.shape
    pad_size = min(w, h) - 1
    pad = torch.nn.ReflectionPad2d(pad_size)
    image = image.transpose(2, 0, 1)
    image_tensor = torch.from_numpy(image)
    image_tensor = image_tensor.unsqueeze(0).type(torch.float32)
    image_tensor = pad(image_tensor)
    print("image_tensor_type: ", type(image_tensor))
    print("image_tensor_shape: ", image_tensor.size())
    rot_angel = angle
    rot_image = F.rotate(image_tensor, rot_angel, interpolation=F.InterpolationMode.BILINEAR)
    rot_image = F.rotate(rot_image, -rot_angel, interpolation=F.InterpolationMode.BILINEAR)
    #rot_image = F.rotate(image_tensor, 3, interpolation=F.InterpolationMode.BILINEAR)
    #rot_image = F.rotate(rot_image, -3, interpolation=F.InterpolationMode.BILINEAR)
    rot_image = rot_image.squeeze(0)
    print("rot_image_size: ", rot_image.size())
    rot_out = rot_image.numpy()
    rot_out = rot_out.transpose(1, 2, 0)
    rot_out = rot_out[pad_size:pad_size+h, :]
    print(rot_out.shape)
    rot_out = rot_out[:, pad_size:pad_size+w]
    print(rot_out.shape)
    return rot_out
