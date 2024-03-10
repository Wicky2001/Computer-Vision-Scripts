import os

import cv2
"""
In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.
"""

img = cv2.imread(os.path.join('.', 'birds.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#convert black birds to white and white background to black
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

#geting the margin of the white objects
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        # cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)

        #getiing the bounding boxes of the contours
        x1, y1, w, h = cv2.boundingRect(cnt)

        #draw a rectangle around objects
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
