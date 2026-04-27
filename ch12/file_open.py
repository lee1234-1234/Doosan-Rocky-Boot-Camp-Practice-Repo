# file_open.py

import os

# 작업디렉터리 확인
print(os.getcwd())

# "\n" : 줄바꿈(newline)
# r : raw(날것의, 원형의)

f = open("C:/ch12/file.txt")
f = open(r"C:\ch12\file.txt")
f = open(r"ch12\file_open.py")

# f.메서드명()  # 파일객체 멤버함수
# f.변수명      # 파일객체 멤버변수

# 파일 닫기
f.close()