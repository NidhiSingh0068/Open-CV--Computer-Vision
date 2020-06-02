##Joining Images

import cv2
import numpy as np

img = cv2.imread("Resources/lam.jpg")

#imgHor = np.hstack((img,img))
#imgVer = np.vstack((img,img))


#cv2.imshow("Horinzontal",imgHor)
#cv2.imshow("Vertical",imgVer)





cv2.waitKey(0)