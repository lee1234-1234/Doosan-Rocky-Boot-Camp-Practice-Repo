# 7. 주어진 리스트에서 next() 함수를 사용하여 각 요소를 하나씩 출력하세요. 
# StopIteration 예외를 처리하여 출력이 끝날 때까지 반복되도록 하세요.
# fruits = ["apple", "banana", "cherry"]


fruits = ["apple", "banana", "cherry"]

foods = iter(fruits)

while True:
    try:
        print(next(foods))
    except StopIteration:
        break