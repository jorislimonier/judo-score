import tensorflow as tf
from tf_bodypix.api import download_model, load_model, BodyPixModelPaths
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def bodypix_segmentation():
    bodypix_model = load_model(download_model(
        BodyPixModelPaths.RESNET50_FLOAT_STRIDE_16
    ))
    result = bodypix_model.predict_single(image_array)
    colored_mask = result.get_colored_part_mask(mask)

    return colored_mask
