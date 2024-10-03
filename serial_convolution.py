import cv2
import numpy as np
import time
import os


def apply_sobel_filter(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = np.sqrt(sobelx**2 + sobely**2)
    return sobel_combined


def process_images_serial(image_folder, num_images):
    images = os.listdir(image_folder)[:num_images]  
    start_time = time.time()
    




    for img_name in images:
        img_path = os.path.join(image_folder, img_name)
        img = cv2.imread(img_path)
        if img is not None:
            apply_sobel_filter(img) 
    



    end_time = time.time()
    return (end_time - start_time) * 1000  
