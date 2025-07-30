# Learning how to resize and image using OpenCV
import cv2
import os

img= cv2.imread(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-3\Basic-Operations\Data\dog.png')
cv2.imshow('Original Image', img)
#(Height, Width, Channels)
print("Original Dimensions : ", img.shape)
cv2.waitKey(0)

# Resizing the image
# (Width,Height)
resized_img=cv2.resize(img,(500,500))
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
print("Resized Dimensions : ", resized_img.shape)