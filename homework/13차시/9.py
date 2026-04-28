# 9. 문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러가 발생합니다. 
# 예외처리를 통해 에러가 발생하는 PER은 0으로 출력하세요.
# per = ["10.31", "", "8.00"]
# for i in per:
#     print(float(i))

per = ["10.31", "", "8.00"]
for i in per:
    try: 
        print(float(i))
    except ValueError:
        print(0)