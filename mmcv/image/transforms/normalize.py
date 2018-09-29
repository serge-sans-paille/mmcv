import numpy as np

from .colorspace import bgr2rgb, rgb2bgr

__all__ = ['imnorm', 'imdenorm']


def imnorm(img, mean, std, to_rgb=True):
    img = img.astype(np.float32)
    if to_rgb:
        img = bgr2rgb(img)
    return (img - mean) / std


def imdenorm(img, mean, std, to_bgr=True):
    img = (img * std) + mean
    if to_bgr:
        img = rgb2bgr(img)
    return img