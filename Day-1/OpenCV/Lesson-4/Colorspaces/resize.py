#Using previous lessons to resize an image
# Learning how to resize and image using OpenCV
import cv2
import os

img= cv2.imread(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-4\Colorspaces\Data\scene.png')
#(Height, Width, Channels)
print("Original Dimensions : ", img.shape)

# Resizing the image
# (Width,Height)

resized_img=cv2.resize(img,(700,700))
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
print("Resized Dimensions : ", resized_img.shape)
img_output_path = os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-4\Colorspaces\Data\scene_output.png')
if(not os.path.exists(img_output_path)):
    cv2.imwrite(img_output_path, resized_img)
    print("Image saved successfully at:", img_output_path)
else:
    print("resized_imgImage already exists at:", img_output_path)




