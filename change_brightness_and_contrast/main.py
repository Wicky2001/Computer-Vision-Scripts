import cv2
alpha = 1.5 # Contrast control
beta = 5 # Brightness control

img = cv2.imread(r"C:\Users\Wicky\Documents\GitHub\Innovation_competition\ocr_part\low_bright_ness.jpeg")

adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)