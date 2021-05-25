from PIL import Image
from collections.abc import Callable
from pathlib import Path
from pytube import YouTube
from tf_bodypix.api import download_model, load_model, BodyPixModelPaths
from viz import *
import cv2 as cv
import cv2 as cv
import keras_segmentation.pretrained as seg_models
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import random
import tensorflow as tf
import time

# %% Throw-away functions


def download_sample_video():
    youtube = YouTube("https://youtu.be/GgO4-din03U")
    video = youtube.streams.first()
    video.download()


def extract_frames(video_path):
    video_path = Path("data/sample_fight.mp4")
    capture = cv.VideoCapture(str(video_path))
    i = 0

    while capture.isOpened():
        ret, frame = capture.read()
        cv.imwrite(f"data/frames/frame_{i}.jpg", frame)
        i += 1


# %%
@load_image
def show_image(image):
    return image


@load_image
def bodypix_segmentation(image):
    bodypix_model = load_model(
        download_model(BodyPixModelPaths.RESNET50_FLOAT_STRIDE_16)
    )
    result = bodypix_model.predict_single(image)
    mask = result.get_mask(threshold=0.75)
    colored_mask = result.get_colored_part_mask(mask)

    return colored_mask


def segment_image(model):
    return lambda path: model.predict_segmentation(inp=str(path))


vignettes(show_image, "normal")

vignettes(segment_image(seg_models.pspnet_50_ADE_20K()), "pspnet_50_ADE_20K")

vignettes(segment_image(seg_models.pspnet_101_cityscapes()), "pspnet_101_cityscapes")

vignettes(segment_image(seg_models.pspnet_101_voc12()), "pspnet_101_voc12")
