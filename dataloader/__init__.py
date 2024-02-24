import torch.utils.data
import torchvision

from .hico_det import build


def build_dataset(image_set):
    return build(image_set)