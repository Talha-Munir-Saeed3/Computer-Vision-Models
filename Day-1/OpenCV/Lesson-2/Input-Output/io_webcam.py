import cv2

#1. Read webcam input
#Numbers indiacate the webcam we want to access
webcam = cv2.VideoCapture(0)
print("Webcam opened:", webcam.isOpened())

#2. Capture frames from the webcam
while True:
    ret , frame = webcam.read()
    cv2.imshow('Webcam Frame', frame)
    #Letter Q will terminate the execution of the webcam
    #Again Time Depends in the FPS of the webcam
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows 
