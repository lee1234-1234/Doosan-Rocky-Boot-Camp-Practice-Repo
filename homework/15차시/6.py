# 6. 주어진 리스트를 이터레이터로 변환하고, 
# 각 요소를 하나씩 출력하는 프로그램을 작성하세요.
# numbers = [1, 2, 3, 4, 5]


numbers = [1, 2, 3, 4, 5]

number = iter(numbers)

for item in number:
    print(item)