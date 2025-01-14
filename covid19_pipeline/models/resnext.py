import math
from functools import partial

import torch
import torch.nn as nn
import torch.nn.functional as F

from .resnet import conv1x1x1, Bottleneck, ResNet
from .utils import partialclass

from torchline.models import META_ARCH_REGISTRY


__all__ = ['resnext3d']


def get_inplanes():
    return [128, 256, 512, 1024]


class ResNeXtBottleneck(Bottleneck):
    expansion = 2

    def __init__(self, in_planes, planes, cardinality, stride=1,
                 downsample=None):
        super().__init__(in_planes, planes, stride, downsample)

        mid_planes = cardinality * planes // 32
        self.conv1 = conv1x1x1(in_planes, mid_planes)
        self.bn1 = nn.BatchNorm3d(mid_planes)
        self.conv2 = nn.Conv3d(mid_planes,
                               mid_planes,
                               kernel_size=3,
                               stride=stride,
                               padding=1,
                               groups=cardinality,
                               bias=False)
        self.bn2 = nn.BatchNorm3d(mid_planes)
        self.conv3 = conv1x1x1(mid_planes, planes * self.expansion)


class ResNeXt(ResNet):

    def __init__(self,
                 block,
                 layers,
                 block_inplanes,
                 n_input_channels=3,
                 conv1_t_size=7,
                 conv1_t_stride=1,
                 no_max_pool=False,
                 shortcut_type='B',
                 cardinality=32,
                 classes=400):
        block = partialclass(block, cardinality=cardinality)
        super().__init__(block, layers, block_inplanes, n_input_channels,
                         conv1_t_size, conv1_t_stride, no_max_pool,
                         shortcut_type, 
                         classes)

        #self.fc = nn.Linear(cardinality * 32 * block.expansion, classes)
        self.fc = nn.Linear(6144, classes)


def generate_model(model_depth, **kwargs):
    assert model_depth in [50, 101, 152, 200]

    if model_depth == 50:
        model = ResNeXt(ResNeXtBottleneck, [3, 4, 6, 3], get_inplanes(),
                        **kwargs)
    elif model_depth == 101:
        model = ResNeXt(ResNeXtBottleneck, [3, 4, 23, 3], get_inplanes(),
                        **kwargs)
    elif model_depth == 152:
        model = ResNeXt(ResNeXtBottleneck, [3, 8, 36, 3], get_inplanes(),
                        **kwargs)
    elif model_depth == 200:
        model = ResNeXt(ResNeXtBottleneck, [3, 24, 36, 3], get_inplanes(),
                        **kwargs)

    return model

@META_ARCH_REGISTRY.register()
def resnext3d(cfg):
    return generate_model(cfg.model.model_depth,
                          classes=cfg.model.classes,
                          n_input_channels=cfg.model.n_input_channels)
