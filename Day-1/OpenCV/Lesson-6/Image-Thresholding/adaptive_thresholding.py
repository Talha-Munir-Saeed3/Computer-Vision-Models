import cv2
import os
img=cv2.imread(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-6\Image-Thresholding\Data\chess.png')
cv2.imshow('Original Image', img)

#Applying Global Threshold
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Thresholding', thresh)

#Applying Adaptive Threshold
#1.ADAPTIVE_THRESH_GAUSSIAN_C 2.ADAPTIVE_THRESH_MEAN_C

#Should use a more complex image
at= cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,21,30)
cv2.imshow('Adaptive Thresholding', at)
cv2.waitKey(0)

#Saving Images
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-6\Image-Thresholding\Data\New_Data\Adapative_Threshold','adaptive_threshold.png'), at)
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-6\Image-Thresholding\Data\New_Data\Adapative_Threshold','thresh.png'), thresh)
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-6\Image-Thresholding\Data\New_Data\Adapative_Threshold','img_gray.png'), img_gray)
