# set1.py
# set(세트): 중복을 허용하지 않는 자료구조
# 문법: {데이터1, 데이터2, 데이터3}

numbers = {1, 2, 3, 3, 4}
print(numbers)

numbers.add(5)
print(numbers)
numbers.remove(3)
print(numbers)


print("---------------")
# 집합 연산
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 교집합: &
print(set1 & set2)

# 합집합: |
print(set1 | set2)

# 차집합: -
print(set1 - set2)