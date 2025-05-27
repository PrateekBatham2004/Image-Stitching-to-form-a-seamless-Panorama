import cv2
import numpy as np
from utils.sift_stitching import stitch_all_images

if __name__ == "__main__":
    image_files = [
        "images/img_01.jpg",
        "images/img_02.jpg",
        "images/img_03.jpg"
    ]

    panorama = stitch_all_images(image_files)
    if panorama is not None:
        print("Panorama created successfully!")
        cv2.imwrite("output/panorama.jpg", panorama)
    else:
        print("Panorama stitching failed.")