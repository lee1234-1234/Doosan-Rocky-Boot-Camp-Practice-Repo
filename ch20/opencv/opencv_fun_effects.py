# opencv_fun_effects.py

import cv2
import numpy as np
from pathlib import Path

# 현재 py 파일이 있는 폴더 기준으로 이미지 찾기
base_dir = Path(__file__).parent
image_path = base_dir / "sample.jpg"

image = cv2.imread(str(image_path))

if image is None:
    print("이미지를 불러오지 못했습니다.")
    print(image_path)
    exit()

# 창에 너무 크게 뜨지 않게 보여주는 함수
def show_image(title, img, width=500):
    h, w = img.shape[:2]
    ratio = width / w
    resized = cv2.resize(img, (width, int(h * ratio)))
    cv2.imshow(title, resized)


# 1. 만화 느낌 효과
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.medianBlur(gray, 7)

edges = cv2.adaptiveThreshold(
    gray_blur,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    9,
    9
)

color = cv2.bilateralFilter(image, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)


# 2. 픽셀 아트 느낌
h, w = image.shape[:2]

small = cv2.resize(image, (w // 20, h // 20), interpolation=cv2.INTER_LINEAR)
pixel_art = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)


# 3. 좌우 거울 대칭 효과
left = image[:, :w // 2]
mirror = cv2.hconcat([left, cv2.flip(left, 1)])


# 4. 물결 효과
map_y, map_x = np.indices((h, w), dtype=np.float32)

map_x = map_x + 20 * np.sin(map_y / 30)

wave = cv2.remap(
    image,
    map_x,
    map_y,
    cv2.INTER_LINEAR,
    borderMode=cv2.BORDER_REFLECT
)


# 결과 출력
show_image("Original Image", image)
show_image("Cartoon Effect", cartoon)
show_image("Pixel Art Effect", pixel_art)
show_image("Mirror Effect", mirror)
show_image("Wave Effect", wave)

cv2.waitKey(0)
cv2.destroyAllWindows()