# 8. OpenCV를 사용하여 이미지 불러오고 화면에 출력하기

import cv2

# 이미지 파일 경로
image = cv2.imread(r"people.jpg")

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()