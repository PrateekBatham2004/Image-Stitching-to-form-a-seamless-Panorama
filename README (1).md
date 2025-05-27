# 🧵 Image Stitching Panorama Project

This project demonstrates how to generate a seamless panorama from multiple images using SIFT feature detection, keypoint matching, and homography transformation.

Originally developed and tested on Google Colab, it has been converted into a local Python script-based GitHub-uploadable folder.

## 🔗 Colab Notebook Link
[Open in Colab](https://colab.research.google.com/drive/1XnkKwaiv0qX0a25CTxJZfI6FMtT8XJ1C?usp=sharing)

## 📌 Project Features

### 📷 Image Preparation & Visualization
- Load image pairs.
- Convert to RGB and grayscale.
- Visualize input image pairs side-by-side.

### 🔍 SIFT Keypoint Detection
- Detect keypoints and compute descriptors using `cv2.SIFT_create()`.
- Visualize detected keypoints on grayscale images.

### 🎯 Keypoint Matching
- Match descriptors using:
  - Brute-Force Matching with `cv2.BFMatcher` and cross-check.
  - KNN Matching with Lowe’s ratio test.

### 🧮 Homography Estimation
- Use matched keypoints to compute a homography matrix with RANSAC.
- Transform one image onto the plane of the other using `cv2.warpPerspective`.

### 🧵 Panorama Stitching
- Combine warped images with original inputs to create a wide-angle panorama.
- Fallback to `cv2.Stitcher_create()` if feature matching fails.

### 🧩 Modular Project Structure
- Clean separation into modules for loading, matching, warping, and visualization.
- Single-entry `main.py` file provided for running the complete pipeline.

### 📂 Output Directory
- All outputs (keypoint visualizations, matches, panoramas) are saved in the `/output/` directory.

---

## 📝 Notes
- Ensure input images have sufficient overlapping regions and features.
- Tuning feature detector and matcher parameters may improve results.
- The modular structure enables quick testing of alternative methods.
