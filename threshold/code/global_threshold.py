"""
retval, dst = cv2.threshold(src, thresh, maxvalue, type)
src: This is the source image (single-channel, grayscale).
thresh: This is the threshold value. Pixels with intensity values greater than thresh will be set to a value defined by the type parameter.
maxvalue: This is the maximum value that can be assigned to a pixel. This value is used when the pixel value is above the threshold.
type: This is the thresholding type. It specifies how pixel values are determined to be above or below the threshold.
"""
import os

import cv2


img = cv2.imread(os.path.join('.', 'bear.jpg'))


#Binary Thresholding
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
""" 
Binary Thresholding (cv2.THRESH_BINARY):

In this method, pixel values above the threshold are set to a maximum value (maxval), and pixel values below the threshold are set to zero.
Syntax: cv2.THRESH_BINARY
"""
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

thresh = cv2.blur(thresh, (10, 10))

#blur the threshed image to remove the noice in the background
ret, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)

