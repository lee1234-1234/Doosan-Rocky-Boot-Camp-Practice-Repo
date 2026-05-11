# opencv_resize.py

import cv2

image = cv2.imread(r'ch20\opencv\sample.jpg')

# edges = cv2.Canny(image, threshold1=100, threshold2=200)
edges = cv2.Canny(image, threshold1=10, threshold2=200)

cv2.imshow('Edge detected Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()