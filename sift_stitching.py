import cv2
import numpy as np

sift = cv2.SIFT_create()

def stitch_images(base_img, new_img):
    kp1, des1 = sift.detectAndCompute(base_img, None)
    kp2, des2 = sift.detectAndCompute(new_img, None)

    flann = cv2.FlannBasedMatcher(dict(algorithm=1, trees=5), dict(checks=50))
    matches = flann.knnMatch(des1, des2, k=2)

    good = [m for m, n in matches if m.distance < 0.7 * n.distance]
    if len(good) < 4:
        print("Not enough matches!")
        return None

    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    H, _ = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 4.0)

    height, width = base_img.shape[:2]
    panorama = cv2.warpPerspective(new_img, H, (width + new_img.shape[1], height))
    panorama[0:height, 0:width] = base_img
    return panorama

def stitch_all_images(image_files):
    images = [cv2.imread(img) for img in image_files]
    for i, img in enumerate(images):
        if img is None:
            print(f"Could not load {image_files[i]}")
            return None

    panorama = images[0]
    for i in range(1, len(images)):
        panorama = stitch_images(panorama, images[i])
        if panorama is None:
            return None
    return panorama