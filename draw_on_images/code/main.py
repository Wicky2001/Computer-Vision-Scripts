import os

import cv2


img = cv2.imread(os.path.join('.', 'whiteboard.png'))

print(img.shape)

# line
#syantax-: cv2.line(img, starting_point->(x, y), end_point->(x ,y), line_color_BGR->(0, 255, 0), line_width->3)
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

# rectangle

#Syntax-: cv2.rectangle(image, upper_left_corner, bottom_right_coner, color,width)

#when width = -1 the inside of the rectangle is also filled
cv2.rectangle(img, (200, 350), (450, 600), (0, 0, 255), -1)

cv2.rectangle(img, (100, 200), (300, 700), (0, 255,0), 1)


# circle
#Syntax-: cv2.rectangle(image, center, radius, color,width)
cv2.circle(img, (800, 200), 75, (255, 0, 0), 10)

# text
#Syntax-: cv2.putText(image, starting_point, font_style, font_size,color,width)
cv2.putText(img, 'Hey you!', (600, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 5)

cv2.imshow('img', img)
cv2.waitKey(0)
