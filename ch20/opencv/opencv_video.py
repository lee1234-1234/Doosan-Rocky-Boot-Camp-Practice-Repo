# opencv_video.py

import cv2

cap = cv2.VideoCapture(r"ch20\opencv\turtle.mp4")

while True:
    # 이미지 파일 읽기
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('Loaded Image', frame)
    cv2.waitKey(10)     # 대기시간(ms)


cap.release()           # 비디오 장치 사용 후 자원을 해제
cv2.destroyAllWindows() # 모든 