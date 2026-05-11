# opencv_resize.py

import cv2

image = cv2.imread(r'ch20\opencv\sample.jpg')

resized = cv2.resize(image, (300, 300))

cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()