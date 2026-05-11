# opencv_color.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\sample.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Gray 방식
# 1채널만 사용(밝기만 표현) 255 흰색 ~ 0 검정
# 이미지 연산의 양을 줄여서 속도를 높이는데 필요