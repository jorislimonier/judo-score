from model_tester import map_vignette, frames
import cv2 as cv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# OpenCV HSV scale: (180, 255, 254)
light_navy_blue = (90, 100, 40)
dark_navy_blue  = (140, 200, 200)

# OpenCV HSV scale: (180, 255, 254)
light_white = (0, 0, 100)
dark_white  = (155, 100, 255)

blue_mask = lambda hsv: cv.inRange(hsv, light_navy_blue, dark_navy_blue)
white_mask = lambda hsv: cv.inRange(hsv, light_white, dark_white)

def apply_mask(mask):
    @load_image
    def _apply_mask(image):
        hsv_image = cv.cvtColor(image, cv.COLOR_RGB2HSV)
        calibrated_mask = mask(image)
        masked_img = cv.bitwise_and(image, image, mask=calibrated_mask)

        return masked_img

    return _apply_mask


# %% K-means clustering
mat_yellow = (215, 214, 140)
navy_blue_gi = (39, 73, 137)
white_gi = (183, 186, 199)
red_logo = (192, 86, 134)
dark_background = (20, 28, 51)
ad_color = (111, 133, 203)

initial_clusters = np.array([
    white_gi,
    navy_blue_gi,
    mat_yellow,
    red_logo,
    dark_background,
    ad_color
])

n_clusters = 6

@load_image
def kmeans_color_clustering(image):
    reshaped = image.reshape((-1, 3))

    clt = KMeans(n_clusters=6, init=initial_clusters)
    clt.fit(reshaped)

    colors = clt.cluster_centers_
    segmented_image = np.array([colors[clt.labels_[i]] for i in range(len(clt.labels_))])
    segmented_image = segmented_image.reshape((360, 640, 3)) / 255.

    return segmented_image


# TODO
# def srgb(c1, c2):
#     return (c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2 + (c2[2] - c1[2]) ** 2
#
# @load_image
# def kmeans_keep_players(image):
#     image = plt.imread(frames[3])
#     reshaped = image.reshape((-1, 3))
#
#     clt = KMeans(n_clusters=6, init=initial_clusters)
#     clt.fit(reshaped)
#
#     colors = clt.cluster_centers_
#     segmented_list = np.array([colors[clt.labels_[i]] for i in range(len(clt.labels_))])
#     segmented_image = segmented_list.reshape((360, 640, 3))
#
#     stack = np.array([white_gi] * 6)
#     index = np.argmin(srgb(stack.transpose(), colors.transpose()))
#     bitmask = (segmented_image == colors[index]).astype(np.int32)
#
#     masked_image = cv.bitwise_and(image, image, bitmask)
#     plt.imshow(masked_image)
#
#     segmented_image = segmented_image.reshape((360, 640, 3)) / 255.
#     plt.imshow(segmented_image)
#
#     return segmented_image
#
# def kmeans_keep_white_blue(path):
#     kmeans_color_clustering(path)
#
# clustered = kmeans_color_clustering(path)


map_vignette(apply_mask(white_mask), "white_player")

map_vignette(apply_mask(blue_mask), "blue_player")

map_vignette(kmeans_color_clustering, "kmeans")
