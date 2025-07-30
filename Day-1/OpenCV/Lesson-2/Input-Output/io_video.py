import cv2

#Read a video from a file
video_path = r'C:\Users\Talha\Desktop\CODES\DLP\Computer-Vision-Models\Day-1\OpenCV\Lesson-2\Input-Output\Data\Paladins_Omen.mp4'
video = cv2.VideoCapture(video_path)

print("Video opened:", video.isOpened())
print("Video Frame Rate:", video.get(cv2.CAP_PROP_FPS))
#Visualize the video 
ret=True
while ret:
    #Video.Read() Function returns 2 variables
    #Frame
    #Ret is a boolean value indicating if the frame was read successfully
    #If ret is False, it means the video has ended or there was an error
    ret, frame = video.read()
    if ret:
        cv2.imshow('Video Frame', frame)
        #wait for 30 milliseconds before showing the next frame
        cv2.waitKey(30)

#4. Release the video capture object,memory and close all OpenCV windows       
video.release()  
cv2.destroyAllWindows()         
