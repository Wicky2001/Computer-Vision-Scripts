import os

import cv2
import numpy as np


img = cv2.imread(os.path.join('.', 'player.jpg'))

#edge detector
img_edge = cv2.Canny(img, 100, 200)

#increase the width of the detected edges
img_edge_d = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8))

#decrease the width of the image
img_edge_e = cv2.erode(img_edge_d, np.ones((3, 3), dtype=np.int8))

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)
cv2.waitKey(0)
