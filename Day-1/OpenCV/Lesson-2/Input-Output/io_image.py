import cv2
import os

#1. Read an image from a file
#Joins multiple paths together
image_path = os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-2\Input-Output', 'Data', 'dog.png')
image = cv2.imread(image_path)
print("Image shape:", image.shape)

#2. Write the image to a file
img_output_path = os.path.join(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-2\Input-Output', 'Data', 'dog_output.png')

#If Images does not exist, it will create a new one
if(not img_output_path):
    cv2.imwrite(img_output_path, image)
    print("Image saved successfully at:", img_output_path)
else:
    print("Image already exists at:", img_output_path)

#3 Display the image in a window
cv2.imshow('Dog Image', image)
# Wait for a key press and close the window
cv2.waitKey(0)

#0 means wait indefinitely can be ms

# If failing to close the window, it opens and it and immediately closes

