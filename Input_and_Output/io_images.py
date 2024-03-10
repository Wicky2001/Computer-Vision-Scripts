import os

import cv2

#read image
image_path = os.path.join("..","data","car.jpg")
img = cv2.imread(image_path)

#write an image
cv2.imwrite(os.path.join("..","data","car_out.jpg"),img)

#visualize an image
cv2.imshow("window name",img)
cv2.waitKey(0)


