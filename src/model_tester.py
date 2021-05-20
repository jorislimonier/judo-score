from PIL import Image
from pathlib import Path
from pytube import YouTube
import cv2 as cv
import keras_segmentation.pretrained as seg_models
import matplotlib.pyplot as plt
import numpy as np
import random
import time

# %% Preparation functions
def download_sample():
    youtube = YouTube("https://youtu.be/GgO4-din03U")
    video = youtube.streams.first()
    video.download()

def extract_frames(video):
    video_path = Path("data/sample_fight.mp4")
    capture = cv.VideoCapture(str(video_path))
    i = 0

    while capture.isOpened():
        ret, frame = capture.read()
        cv.imwrite(f"data/frames/frame_{i}.jpg", frame)
        i += 1


# %%
from collections.abc import Callable

vignette_side = 4
extracted_frames = list(Path("data/frames").glob("*"))
frames = random.sample(extracted_frames, vignette_side ** 2)

def map_vignette(image_transform, title: str) -> None:
    t_start = time.time()

    plt.figure(figsize=(10, 10))
    for i, jpg in enumerate(frames):
        plt.subplot(vignette_side, vignette_side, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        transform = image_transform(jpg)
        plt.imshow(transform)

    t_end = time.time()
    duration = t_end - t_start
    plt.suptitle(f"{title} {duration:0.2f}s /{duration/vignette_side ** 2: 0.2f}s",
                 y=0.93, fontsize=21)
    plt.savefig(title)


def load_image(func):
    def wrapper(path):
        image = plt.imread(path)
        return func(image)

    return wrapper

@load_image
def show_image(image):
    return image

# %%
def segment_image(model):
    return lambda path: model.predict_segmentation(inp=str(path))

# Sample images
map_vignette(show_image, "normal")

# %% Then segment them
# map_vignette(segment_image(seg_models.pspnet_50_ADE_20K()), "pspnet_50_ADE_20K")
#
# map_vignette(segment_image(seg_models.pspnet_101_cityscapes()), "pspnet_101_cityscapes")
#
# map_vignette(segment_image(seg_models.pspnet_101_voc12()), "pspnet_101_voc12")
#
# models = {
#     "pspnet_50_ADE_20K": pspnet_50_ADE_20K,
#     "pspnet_101_cityscapes": pspnet_101_cityscapes,
#     "pspnet_101_voc12": pspnet_101_voc12
# }
