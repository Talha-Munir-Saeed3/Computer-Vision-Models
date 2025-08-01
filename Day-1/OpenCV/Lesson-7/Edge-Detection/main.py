#Using OpenCV for Edge Detection
import cv2
import os
import numpy as np

#There are three types of edge detection methods in OpenCV
#1. Canny Edge Detection
#2. Sobel Edge Detection
#3. Laplacian Edge Detection

img= cv2.imread(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-7\Edge-Detection', 'Data', 'image.png'))
cv2.imshow('Original Image', img)

#Trial and Error approach to find the best parameters for Canny Edge Detection
#Canny Edge Detection requires two parameters: threshold1 and threshold2
#These thresholds are used to identify strong and weak edges in the image

#This number help in identifying details
img_canny = cv2.Canny(img, 150, 250)
cv2.imshow('Canny Edge Detection', img_canny)

#Making everything thicker and more visible
img_dilated = cv2.dilate(img_canny, np.ones((2,2), np.uint8), iterations=1)
cv2.imshow('Dilated Image', img_dilated)

#Opposite of dilation is erosion
#Erosion removes pixels on object boundaries
img_eroded = cv2.erode(img_dilated, np.ones((2,2), np.uint8), iterations=1)
cv2.imshow('Eroded Image', img_eroded)
cv2.waitKey(0)

#Save Images
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-7\Edge-Detection\Data', 'New_Data', 'canny_edge_detection.png'), img_canny)
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-7\Edge-Detection\Data', 'New_Data', 'dilated_image.png'), img_dilated)
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-7\Edge-Detection\Data', 'New_Data', 'eroded_image.png'), img_eroded)  


