import cv2
import numpy as np
import time
import os
from multiprocessing import Pool, cpu_count


def apply_sobel_filter(image_path):
    img = cv2.imread(image_path)
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sobel_combined = np.sqrt(sobelx**2 + sobely**2)


def process_images_parallel(image_folder, num_images):
    images = [os.path.join(image_folder, img_name) for img_name in os.listdir(image_folder)[:num_images]]
    
    start_time = time.time()
    
    with Pool(cpu_count()) as pool:
        pool.map(apply_sobel_filter, images)
    
    end_time = time.time()
    return (end_time - start_time) * 1000  
