#Cropping an image using OpenCV
import cv2
import os

# Load the image
img = cv2.imread(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-3\Basic-Operations\Data\dog.png')
cv2.imshow('Original Image', img)
cv2.waitKey(0)
print("Original Dimensions : ", img.shape)

#Cropping the image
#Because an image is an numpy array hence coordinates
cropped_img = img[50:200,10:180]  # Adjust the coordinates as needed
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)
print("Cropped Dimensions : ", cropped_img.shape)


