#blur use to remove noice from an image

import os

import cv2


img = cv2.imread(os.path.join('..', 'data','cow-salt-peper.png'))

#k is neighbour size around an image
k_size = 7

#normal blur
img_blur = cv2.blur(img, (k_size, k_size))

#gaussian_blur
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 5)

#median_blur
img_median_blur = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur)
cv2.waitKey(0)