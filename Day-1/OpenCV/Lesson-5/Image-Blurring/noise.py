#Same Code on a grey scale image which has noise 
#Although we could have made a function and only have used the image path but for clarity 

import cv2
import os

img=cv2.imread(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-5\Image-Blurring\Data\grey.png')
cv2.imshow('Original Image',img)
print('Original Image Shape:',img.shape)

#Image Blurring
size=7

#Depending upon the size of the 'size' neighbourhood, the blurring will be more or less
#1. Blur
img_blur=cv2.blur(img,(size,size)) 

#2. Gaussian Blur
img_gaussian=cv2.GaussianBlur(img,(size,size),0) 

#3. Median Blur
img_median=cv2.medianBlur(img,size)

# Show
cv2.imshow('Median Blurred Image',img_median)
cv2.imshow('Gaussian Blurred Image',img_gaussian)
cv2.imshow('Blurred Image',img_blur)
cv2.waitKey(0)

#Saving Images
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-5\Image-Blurring\Data\New_Data','grey_img_blur.png'),img_blur)
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-5\Image-Blurring\Data\New_Data','grey_img_gaussian.png'),img_gaussian)
cv2.imwrite(os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-5\Image-Blurring\Data\New_Data','grey_img_median.png'),img_median)
#Although we cant see any improvements but blurring does help with correct parameters