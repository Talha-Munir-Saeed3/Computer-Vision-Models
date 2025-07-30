#1. Images are numpy arrays
import cv2
# Load an image
image = cv2.imread('path_to_your_image.jpg')
print(type(image))  # This will print <class 'numpy.ndarray'>   

#2. Image shape is given by (height, width, channels)
print(image.shape)  # This will print the dimensions of the image, e.g., (480, 640, 3)

#3. Image consists of pixels
# Access a pixel at (x, y)
# Values for pixel ranges from 0 to 255 for each channel
# Binary image has only one channel Black and White hence 0 or 1
# 16-bit image has values from 0 to 65535
x, y = 100, 50
pixel = image[y, x]


