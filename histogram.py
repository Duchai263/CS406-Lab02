import os
import cv2
import numpy as np

def calcHist(img_path):
    img = cv2.imread(img_path)
    # img = cv2.split(img)
    if img is None:
        print('Could not open or find the image')
        return

    b_hist = cv2.calcHist([img], [0], None, [256], [0,256])
    g_hist = cv2.calcHist([img], [1], None, [256], [0,256])
    r_hist = cv2.calcHist([img], [2], None, [256], [0,256])

    return np.array([b_hist,g_hist,r_hist])

def distanceEuclidian(hist1,hist2):
    return np.linalg.norm(hist1 - hist2)

