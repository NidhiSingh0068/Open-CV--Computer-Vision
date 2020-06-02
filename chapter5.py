##Size of Image

import cv2
import numpy as np

img = cv2.imread("Resources/lam.jpg")
print(img.shape)  #shape of image  (183, 275, 3)

imgResize = cv2.resize(img, (150, 100))
print(imgResize.shape)  #resizing an image -increase or decrease

imgCropped = img[0:100,200:275]  #Cropping an image - (height[starting point:Ending point],width[starting point:Ending point])



cv2.imshow("Image", img)
cv2.imshow(" Resized Image", imgResize)
cv2.imshow("Cropeed Image", imgCropped)

cv2.waitKey(0)