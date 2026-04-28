# string_func.py
# 함수 사용시 확인할 내용
# 1. 기능/동작
# 2. 매개변수
# 3. 반환값

# 문자열.split(구분자)
# 1. 기능/동작 : 구분자 기준 분리
# 2. 매개변수 : 구분자
# 3. 반환값 : 구분된 문자열 -> list
my_string = "Python is a popular programing language"
split_list = my_string.split()
print(split_list)
print(split_list[4])


print("hello\t \"great\" world!!", end="\n")
print("abcde\bthanks!", end="\r")
print("hi")

print("----------------")
"문자열".strip()
# 1. 기능/동작 : 문자열 양 끝 공백문자를 제거
# 2. 매개변수 : 제거할 문자(생략 시 공백)
# 3. 반환값 : 수정된 문자열 -> str
my_string = "   python is awesom!   "
stripped_string = my_string.strip()
print(stripped_string)

my_string = "\t   python is awesom!   \n"
stripped_string = my_string.strip()
print(my_string)
print(stripped_string)

print("----------------")
# "구분자" .join()
# 1. 기능/동작 : iterable의 요소들을 문자열로 연결
# 2. 매개변수 : iterable(문자열 요소 집합)
# 3. 반환값 : 연결된 문자열 -> str
my_list = ["apple", "banana", "cherry"]
joined_string = "-".join(my_list)
print(joined_string)