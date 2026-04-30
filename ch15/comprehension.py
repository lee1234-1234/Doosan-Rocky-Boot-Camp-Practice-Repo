# comprehension.py

# 리스트 컴프리핸션 : 새 리스트 생성
# [표현식 for 요소 in 이터러블 [if 조건]]

numbers = [1, 2, 3, 4]
squared = [x**2 for x in numbers]
print(squared)

# 조건문이 참인 경우, 요소를 포함하여 표현식 수행
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

squared = [x**2+1 for x in numbers if x % 2 == 0]
print(squared)  # [5, 17]

print("--------------------")
# 딕셔너리 컴프리핸션 : 새 딕셔너리 생성
# {key 표현식:value 표현식 for 요소 in 이터러블 [if 조건]}

squared_dict = {x:x**2 for x in range(5)}
print(squared_dict) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

even_squared_dict = {x:x**2 for x in range(10) if x % 2 == 0}
print(even_squared_dict) # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# range(10)이 사용할 애들이야
# 사용할 애들을 if 조건에 맞춰서 해당하는 애만 사용할거야
# 해당하는 애만 식에 대입할거야

subjects = ['수학', '영어', '역사']
scores = {subject:0 for subject in subjects}
print(scores)


print("------------")
# 제너레이터 생성 방법2
# 제너레이터 컴프리핸션: 새 제너레이터 생성
# (표현식 for 요소 in 이터러블 [if 조건])
gen = (i*i for i in range(1, 10))
print(type(gen))

print(next(gen))
for item in gen:
    print(item)
print(next(gen))