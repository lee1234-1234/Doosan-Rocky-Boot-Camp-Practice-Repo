# 10. 다음과 같이 리스트가 주어져 있을 때, 
# numbers = [10, 20, 30]
# 사용자로부터 인덱스를 입력 받아 해당 위치의 원소를 출력하는 프로그램을 작성하시오.
# 범위를 벗어난 인덱스를 입력할 경우 IndexError를 처리하여 
# "잘못된 인덱스입니다." 라는 메시지를 출력하시오.
# 또한 숫자가 아닌 값이 입력으로 들어오는 경우도 예외 처리하시오.

numbers = [10, 20, 30]

try:
    ind = int(input("인덱스를 입력해주세요: "))
    print(numbers[ind])

except ValueError:
    print("숫자를 입력하세요")

except IndexError:
    print("잘못된 인덱스입니다.")