##Warp Perspective

import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")
print(img.shape)

width,height=183,275
pts1 = np.float32([[194,24], [272,70], [130,135], [206,180]])
pts2 = np.float32([[0,0], [width,0], [0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)