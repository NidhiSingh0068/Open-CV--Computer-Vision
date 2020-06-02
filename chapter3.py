##Starting webcam


import cv2    #Importing package for Computer Vision

cap = cv2.VideoCapture(0)  #Id for default is 0
cap.set(3, 640)            #Id for height is 3
cap.set(4,480)             #Id for width is 4
cap.set(10,100)            #Id for brightness id 10
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  #Press q to close
        break
