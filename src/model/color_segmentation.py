from model_tester import map_vignette, frames, load_image
import cv2 as cv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# OpenCV HSV scale: (180, 255, 254)
light_navy_blue = (90, 100, 40)
dark_navy_blue = (140, 200, 200)

# OpenCV HSV scale: (180, 255, 254)
light_white = (0, 0, 100)
dark_white = (155, 100, 255)


def blue_mask(hsv):
    return cv.inRange(hsv, light_navy_blue, dark_navy_blue)


def white_mask(hsv):
    return cv.inRange(hsv, light_white, dark_white)


def apply_mask(mask):
    @load_image
    def _apply_mask(image):
        hsv_image = cv.cvtColor(image, cv.COLOR_RGB2HSV)
        calibrated_mask = mask(hsv_image)
        masked_img = cv.bitwise_and(image, image, mask=calibrated_mask)

        return masked_img

    return _apply_mask


# %% K-means clustering

initial_clusters = {
    "yellow_mat": (215, 214, 140),
    "navy_blue_gi": (39, 73, 137),
    "white_gi": (183, 186, 199),
    "red_logo": (192, 86, 134),
    "dark_background": (20, 28, 51),
    "ad_color": (111, 133, 203),
}

centroids = np.array(list(initial_clusters.values()))
n_clusters = len(initial_clusters)


@load_image
def kmeans_color_clustering(image):
    reshaped = image.reshape((-1, 3))

    clt = KMeans(n_clusters=n_clusters, init=centroids)
    clt.fit(reshaped)

    colors = clt.cluster_centers_
    clustered_image = np.array(
        [colors[clt.labels_[i]] for i in range(len(clt.labels_))]
    )
    clustered_image = clustered_image.reshape((360, 640, 3)) / 255.0

    return clustered_image


# Color distance
def srgb(c1, c2):
    return (c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2 + (c2[2] - c1[2]) ** 2


@load_image
def kmeans_keep_players(image):
    reshaped_2d = image.reshape((-1, 3))

    clt = KMeans(n_clusters=n_clusters, init=centroids)
    clt.fit(reshaped_2d)

    colors = clt.cluster_centers_
    clustered_image = np.array(
        [colors[clt.labels_[i]] for i in range(len(clt.labels_))]
    )
    image = clustered_image.reshape((360, 640, 3))

    # Find the k-means color (centroid) that matches the original gi the closest.
    # Make a mask out of all the pixels belonging to this cluster.
    def bitmask_from(color):
        distance_to_color = srgb(
            np.array([color] * n_clusters).transpose(), colors.transpose()
        )
        index_centroid = np.argmin(distance_to_color)
        belongs_to_cluster = image == colors[index_centroid]
        bitmask = (
            belongs_to_cluster[:, :, 0]
            & belongs_to_cluster[:, :, 1]
            & belongs_to_cluster[:, :, 2]
        )
        return bitmask

    mask_union = bitmask_from(initial_clusters["navy_blue_gi"]) | bitmask_from(
        initial_clusters["white_gi"]
    ).astype(np.int8)
    masked_image = cv.bitwise_and(image, image, mask=mask_union)
    masked_image /= 255.0

    return masked_image


map_vignette(apply_mask(white_mask), "custom_mask_white")

map_vignette(apply_mask(blue_mask), "custom_mask_blue")

map_vignette(kmeans_color_clustering, "kmeans_clustering")

map_vignette(kmeans_keep_players, "kmeans_only_players")
