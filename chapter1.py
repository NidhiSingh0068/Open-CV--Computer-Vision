##Displaying image

##Displaying image

import cv2  #Importing package for Computer Vision

img = cv2.imread("Resources/sunset.jpg")  #Path of image
cv2.imshow("Output", img)
cv2.waitKey(0)


