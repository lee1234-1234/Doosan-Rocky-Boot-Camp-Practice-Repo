# raise1.py

# raise 예외클래스명(예외정보데이터)

print("raise")

# 예외 발생시키기
# raise NameError('HI There') # 프로그램 중단

try:
    raise NameError('HI There') # 프로그램 중단
except NameError as e:
    print("An exception flew by!")
    print("e: ", e)

print("exit")