import cv2
import numpy as np
import torchvision.transforms.functional as F
import torch

#pad = torch.nn.ReflectionPad2d(2000)

image = cv2.imread('/Users/liujunyuan/HR_to_LR/data/DIV2K_train_HR/0009.png')
image = image.transpose(2, 0, 1)
image_tensor = torch.from_numpy(image)
image_tensor = image_tensor.unsqueeze(0)
print("image_tensor_type: ", type(image_tensor))
print("image_tensor_shape: ", image_tensor.size())
rot_angel = 60
rot_image = F.rotate(image_tensor, rot_angel, interpolation=F.InterpolationMode.NEAREST)
rot_image = F.rotate(rot_image, -rot_angel, interpolation=F.InterpolationMode.NEAREST)
#rot_image = F.rotate(image_tensor, 3, interpolation=F.InterpolationMode.BILINEAR)
#rot_image = F.rotate(rot_image, -3, interpolation=F.InterpolationMode.BILINEAR)
rot_image = rot_image.squeeze(0)
print("rot_image_size: ", rot_image.size())
rot_out = rot_image.numpy()
rot_out = rot_out.transpose(1, 2, 0)
print(rot_out.shape)
cv2.imwrite('/Users/liujunyuan/HR_to_LR/results/test/rotrot0009.png', rot_out)
