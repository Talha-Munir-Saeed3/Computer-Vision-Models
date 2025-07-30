#Main purpose is to understand how images can be represented in different color spaces using OpenCV

import os
import cv2

img=cv2.imread(r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-4\Colorspaces\Data\scene.png')
cv2.imshow('Orignal Image', img)

#   Convert to different color spaces
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)  
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
xyz_img=cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)

#   Display the images
cv2.imshow('HSV Image', hsv_img)
cv2.imshow('LAB Image', lab_img)    
cv2.imshow('Gray Image', gray_img)
cv2.imshow('RGB Image', rgb_img)
cv2.imshow('XYZ Image', xyz_img)
cv2.waitKey(0)
images_to_save = [(hsv_img, 'hsv'),(lab_img, 'lab'),(gray_img, 'gray'),(rgb_img, 'rgb'),(xyz_img, 'xyz')
]
#Something extra (Optional)
#Save Images
path=r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-4\Colorspaces\Data'

output_folder = os.path.join(path, 'New_Images')
try:
    os.makedirs(output_folder, exist_ok=True)
    print(f"Output directory '{output_folder}' ensured (created or already exists).")
except OSError as e:
    print(f"Error creating directory {output_folder}: {e}")
    exit()

for img_data, color_space_name in images_to_save:
    # Construct the output filename, e.g., "scene_hsv.png"
    output_filename = f"scene_{color_space_name}.png"
    full_output_path = os.path.join(output_folder, output_filename)

    # Save the image
    if not os.path.exists(full_output_path):
        print(f"Saving: '{output_filename}' to '{path}'...")
        success = cv2.imwrite(full_output_path, img_data)
        if success:
            print(f"Successfully saved: {output_filename}")
        else:
            print(f"ERROR: Failed to save: {output_filename}")
            # This can happen if the img_data is somehow invalid for saving (though unlikely here)
    else:
        print(f"  Skipping: '{output_filename}' already exists at '{path}'.")