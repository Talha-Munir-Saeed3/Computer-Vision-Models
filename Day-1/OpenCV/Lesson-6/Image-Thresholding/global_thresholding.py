import cv2
import os

#Primary goal to simplify an image by partitioning it into two parts: foreground and background.
#Below threshold value than 0
#Above threshold value than 255

img=cv2.imread(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-6\Image-Thresholding\Data\image.png')
cv2.imshow('Original Image', img)
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
#There are different types of thresholding methods in OpenCV.
#Binary Threshold, TRUNC etc
#Pass the image and the binary threshold values 
ret,thresh = cv2.threshold(img_gray, 130, 255, cv2.THRESH_BINARY)
thresh_blur=cv2.blur(thresh,(7,7))
cv2.imshow('Blurred Thresholding', thresh_blur)
cv2.imshow('Binary Thresholding', thresh)
cv2.imshow('Grayscale Image', img_gray)
cv2.waitKey(0)

#There are going to be some cases where global threshold underperforms
#Saving Images
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-6\Image-Thresholding\Data\New_Data\Global_Threshold','thresh_blur.png'), thresh_blur)
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-6\Image-Thresholding\Data\New_Data\Global_Threshold','thresh.png'), thresh)
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-6\Image-Thresholding\Data\New_Data\Global_Threshold','img_gray.png'), img_gray)






