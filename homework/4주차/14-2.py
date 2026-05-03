import re

email = input("이메일을 입력하세요: ")

p = re.compile(r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$")

if p.match(email):
    print("올바른 이메일 형식입니다.")
else:
    print("올바르지 않은 이메일 형식입니다.")