# opencv_color1.py

import cv2

# 이미지 파일 읽기
image = cv2.imread(r'ch20\opencv\sample.jpg')

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 3채널 -> 1채널
# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # BGR -> RGB
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    # 색상, 채도, 명도

# cv2.imshow('Grayscale Image', gray)
# cv2.imshow('RGB Image', rgb)
cv2.imshow('HSV Image', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# GRAY 방식
# 1채널만 사용(밝기만 표현) 255 흰색 ~ 0 검정
# 이미지 연산의 양을 줄여서 속도를 높이는데 필요
# 변환공식 : Gray = 0.299 x R + 0.587 x G + 0.114 x B
# 채널수 3개 => 1개 줄어듬

# HSV 방식
# RGB와 마찬가지로 3개의 채널을 갖는 색상 이미지 표현법
# 3 채널은 H(Hue, 색조), S(Saturation, 채도), V(Value, 명도)