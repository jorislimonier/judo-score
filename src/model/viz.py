from pathlib import Path
import random
import time
import matplotlib.pyplot as plt

vignette_side = 4
extracted_frames = list(Path("data/frames").glob("*"))
frames = random.sample(extracted_frames, vignette_side ** 2)


def vignettes(image_transform, title: str) -> None:
    """Samples frames, applies transform, and time the whole."""
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
    plt.suptitle(
        f"{title} {duration:0.2f}s /{duration/vignette_side ** 2: 0.2f}s",
        y=0.93,
        fontsize=21,
    )
    plt.savefig(title)


def load_image(func):
    """Function wrapper to load image from path."""

    def wrapper(path):
        image = plt.imread(path)
        return func(image)

    return wrapper
