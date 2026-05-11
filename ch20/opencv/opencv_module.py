# opencv_module.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\sample.jpg')

cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()