"""
he adaptiveMethod decides how the threshold value is calculated:
There are two adaptive methods, and they are listed below

cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.

The blockSize determines the size of the neighbourhood area and C is a constant that is subtracted from the mean or weighted sum of the neighbourhood pixels.

syntax->
adaptive_thresh = cv2.adaptiveThreshold(img_gray, max_Value, adaptive method, thres hold type, block size, constant c)

Note-: block size must be a odd number

"""

import os

import cv2


img = cv2.imread(os.path.join('.', 'handwritten.png'))

#It is mandatory to convert image to gray scale before apply threshold
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
ret, simple_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)


cv2.imshow('img', img)
cv2.imshow('adaptive_thresh', adaptive_thresh)
cv2.imshow('simple_thresh', simple_thresh)
cv2.waitKey(0)