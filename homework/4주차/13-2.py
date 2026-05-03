# 문제 2) map() 함수와 람다 함수를 사용해 
# 리스트 [10, 20, 30, 40, 50]의 각 요소를 제곱한 결과를 
# 출력하는 프로그램을 작성하시오.


numbers = [10, 20, 30, 40, 50]

result = list(map(lambda x: x**2, numbers))

print(result)