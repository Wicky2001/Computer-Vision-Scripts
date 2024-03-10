#Cropping involves cutting out a portion of the original image, discarding the rest.
import os
import cv2

import os
import cv2


img_path = os.path.join("..","data","car.jpg")

#read the image
image = cv2.imread(img_path)
cv2.imshow("Original image",image)
print(image.shape)

#crop the image
cropped_image = image[10:100,10:200]
cv2.imshow("Cropped image",cropped_image)
cv2.waitKey(0)
