import os

import cv2

#read video
video_path = os.path.join("..","data","Sunset.mp4")

video = cv2.VideoCapture(video_path)

#Visualize the read video
ret = True
while ret:
    #read frame from  video
    #ret is a variable that indicate if the frame is successfully read or not
    ret,frame = video.read()
    if ret:
        #visualize the frame
        cv2.imshow("Window name",frame)
        cv2.waitKey(30)

# Release the memory allocated to video capture object and close the window
video.release()
cv2.destroyAllWindows()