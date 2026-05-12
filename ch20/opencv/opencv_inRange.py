# opencv_inRange.py

import cv2
import numpy as np

# 이미지 파일 읽기
image = cv2.imread(r"ch20\opencv\candies.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# H(색조), S(채도), V(명도)
green_lower = np.array([35, 100, 100])
green_upper = np.array([85, 255, 255])

mask = cv2.inRange(hsv, green_lower, green_upper)
result = cv2.bitwise_and(image, image, mask=mask)


# 이미지 창에 표시
cv2.imshow("Green Color Filtering", result)
cv2.waitKey(0)        # 0: 무한대기
cv2.destroyAllWindows()