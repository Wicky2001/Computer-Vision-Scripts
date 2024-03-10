import os

import cv2
#in csv images are originally BGR not RGB

img = cv2.imread(os.path.join('..','data','car.jpg'))

#convert image to Gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#convert image to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Convert image to HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('img', img)
cv2.imshow('img_hsv', img_hsv)
cv2.waitKey(0)

