# TODO: manhunt on keras_segmentation.pretrained
import cv2 as cv
from pytube import YouTube
from pathlib import Path
from PIL import Image
import random
import matplotlib.pyplot as plt
from keras_segmentation.pretrained import pspnet_50_ADE_20K , pspnet_101_cityscapes, pspnet_101_voc12
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
side = 4
all_frames = list(Path("data/frames").glob("*"))
frames = random.sample(all_frames, side ** 2)

def map_vignette(f, title):
    t_start = time.time()

    plt.figure(figsize=(10, 10))
    for i, jpg in enumerate(frames):
        plt.subplot(side, side, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        f(jpg)

    t_end = time.time()
    duration = t_end - t_start
    plt.suptitle(f"{title} {duration:0.2f}s /{duration/side ** 2: 0.2f}s",
                 y=0.93, fontsize=21)
    plt.savefig(title)

# %%
def show_image(path):
    image = plt.imread(path)
    plt.imshow(image)

def segment_image(model):
    def _segment_image(path):
        output = model.predict_segmentation(inp=str(path))
        plt.imshow(output)

    return _segment_image

# Sample images
map_vignette(show_image, "normal")
# Then segment them
map_vignette(segment_image(pspnet_50_ADE_20K()), "pspnet_50_ADE_20K")

map_vignette(segment_image(pspnet_101_cityscapes()), "pspnet_101_cityscapes")

map_vignette(segment_image(pspnet_101_voc12()), "pspnet_101_voc12")

models = {
    "pspnet_50_ADE_20K": pspnet_50_ADE_20K,
    "pspnet_101_cityscapes": pspnet_101_cityscapes,
    "pspnet_101_voc12": pspnet_101_voc12
}
