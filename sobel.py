# -*- coding: utf-8 -*-
"""
Spyder Editor

@author = Tamzid hasan nahid
"""

import numpy as np
import cv2


image_original = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

cv2.imshow("input",image_gray)

[rows, columns] = np.shape(image_gray)
sobel_filtered_image = np.zeros(shape=(rows, columns))
sobel_filtered_x = np.zeros(shape=(rows, columns))
sobel_filtered_y = np.zeros(shape=(rows, columns))

sobel_y = np.array([[-1, -2, -1], 
                    [0, 0, 0], 
                    [1, 2, 1]])

sobel_x = np.array([[-1, 0, 1], 
                    [-2, 0, 2], 
                    [-1, 0, 1]])

filtered_image_y = cv2.filter2D(image_gray, -1, sobel_y)
filtered_image_x = cv2.filter2D(image_gray, -1, sobel_x)

#normalizedImg = np.zeros((rows, columns))
#normalizedImg = cv2.normalize(filtered_image_x,  normalizedImg, 0, 255, cv2.NORM_MINMAX)
#x_img = (255*(filtered_image_x - np.min(filtered_image_x))/np.ptp(filtered_image_x)).astype(int) 
#cv2.normalize(filtered_image_x, filtered_image_x, 0, 255, cv2.NORM_MINMAX)

#print(filtered_image_x)
#cv2.imshow("sobel x",filtered_image_x)

 




for i in range(rows - 2):
    for j in range(columns - 2):
        gx = np.sum(np.multiply(sobel_x, image_gray[i:i + 3, j:j + 3]))
        sobel_filtered_x[i+1,j+1]=gx
        gy = np.sum(np.multiply(sobel_y, image_gray[i:i + 3, j:j + 3])) 
        sobel_filtered_y[i+1,j+1]=gy
        sobel_filtered_image[i + 1, j + 1] = np.sqrt(gx ** 2 + gy ** 2) 

cv2.normalize(sobel_filtered_x, sobel_filtered_x, 0, 255, cv2.NORM_MINMAX)
cv2.normalize(sobel_filtered_y, sobel_filtered_y, 0, 255, cv2.NORM_MINMAX)
        
#print(np.round(sobel_filtered_x).astype(int))
sobel_filtered_x = np.round(sobel_filtered_x).astype(np.uint8)
sobel_filtered_y = np.round(sobel_filtered_y).astype(np.uint8)
cv2.imshow("sobel x",sobel_filtered_x)
cv2.imshow("sobel y",sobel_filtered_y)

ret1,th1 = cv2.threshold(sobel_filtered_image,127,255,cv2.THRESH_BINARY)

cv2.imshow("sobel",th1)
        
cv2.waitKey(0)
cv2.destroyAllWindows()       


