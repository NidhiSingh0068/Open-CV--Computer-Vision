##Shapes and Texts

import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
#print(img.shape)    #It is a grayscale image
#print(img)          #prints image matrix in binary
#img[:] = 255,0,0    #Colour on whole image
#img[200:300,100:300] = 255,0,0    #Colour on some part of image

cv2.line(img,(0,0),(300,300),(0,255,255),3)  #Drawing  a line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,255),3)  #Drawing  a line on whole screen

#cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)  #Drawing a rectangle
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)  #Drawing a color filled rectangle

cv2.circle(img,(400,50),30,(255,255,0),5)  #Drawing a circle

cv2.putText(img,"OpenCV", (300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)  #Text

cv2.imshow("Image",img)
cv2.waitKey(0)