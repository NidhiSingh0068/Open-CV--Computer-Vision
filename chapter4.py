##Functions

import cv2  #Importing package for Computer Vision
import numpy as np

img = cv2.imread("Resources/sunset.jpg")  #Path of image
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Color
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)     #Blurring the image
imgCanny = cv2.Canny(img, 100,100)              #Outline only
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialated Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)

