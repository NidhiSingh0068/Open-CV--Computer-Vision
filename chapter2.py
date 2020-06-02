##Playing a Video

import cv2    #Importing package for Computer Vision
cap = cv2.VideoCapture("Resources/test_video.mp4")  #Path of video

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  #Press q to close
        break
