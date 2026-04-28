# map_func.py

# map(함수, 이터레이터)
# 1. 기능/동작: 이터레이터에 함수 적용
# 2. 매개변수: 적용함수, 이터레이터
# 3. 반환: map객체 (이터레이터)

def square(x):
    return x**2
print(square(3))

print("-------------")
square = lambda x:x**2
print(square(3))

print("-------------")
numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)
print(list(squared_numbers))

print("-------------")
squared_numbers = map(lambda x:x**2, numbers)
print(list(squared_numbers))