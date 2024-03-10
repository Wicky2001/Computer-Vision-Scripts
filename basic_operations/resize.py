import os
import cv2

#Resizing an image involves changing its dimensions while
# preserving the entire content of the original image.
img_path = os.path.join("..","data","car.jpg")

#read the image
image = cv2.imread(img_path)
cv2.imshow("Original image",image)
print(image.shape)

#resize the image

resized_image = cv2.resize(image,(100,100))
#height = 10 / width = 100c
cv2.imshow("Resized image",resized_image)
cv2.waitKey(0)
