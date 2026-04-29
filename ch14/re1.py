# re1.py
# 정규표션식(Regular Expression)
# : 문자열 패턴 정의해서
# 검색, 검사, 치환, 추출 등 수행하는
# 문자열 처리 규칙

# 패턴 : 일정한 규칙성을 가지고 반복적으로 나타나는 형태

import re
# 패턴 객체: "검색대상문자열"에서 패턴의 발견을 도와주는 객체
# 정규표현식을 정의해서 compile() 함수의 인수로 전달하면
# 패턴 객체 반환함.

# 메타문자: 별도의 의미가 담긴 문자

# [] 문자
# - [] 사이에는 대부분 문자(기호) 포함 가능
# - 메타문자도 사용 가능(단, 별도 의미X)
# - (단, 일부 메타문자는 의미가 있음)

# [abc] : a,b,c 중 한개의 문자와 매치

# 정규표현식 문법
# 패턴객체명 = re.compile("정규표현식")   # 패턴(규칙 생성)
# 패턴객체명.match("검색대상 문자열")
# print(매치객체)

# match() 함수: 문자열 처음부터 정규(표현)식과 매치되는지 조사함

# p = re.compile("정규표현식")
# m = 패턴객체명.match("검색대상문자열")
# print(매치객체)

p = re.compile("[abc]")
# m = p.match("a")          # match='a'
# m = p.match("before")     # match='b'
m= p.match("dude")          # None
print(m)
# print(m.group())


print("-----------")
p = re.compile("[ab]")
print(p.match("apple"))     # match='a'
print(p.match("before"))    # match='b'
print(p.match("dude"))      # None


print("-----------")
p = re.compile("ab")
print(p.match("apple"))     # match='a'
print(p.match("banana"))    # match='b'
print(p.match("ba"))        # None
print(p.match("absoulte"))  # match='ab'


print("-----------")
p = re.compile("[0-5]")
print(p.match("1apple"))    # 1
print(p.match("2banana"))   # 2
print(p.match("7lemon"))    # None



print("dot(.)--------")
print("plus(+)-------")
p = re.compile("[.abc]")
print(p.match(".apple"))
p = re.compile("[+abc]")
print(p.match("+banana"))

print("캐럿(^)-------")
p = re.compile("[^abc]")
print(p.match("^apple"))
print(p.match("apple"))
print(p.match("melon"))
print(p.match("amelon"))

print("역슬래시(\)--------")
p = re.compile("[\^abc]")
print(p.match("^apple"))
p = re.compile("[a\-c]")
print(p.match("-apple"))
print(p.match("banana"))

print("역슬래시(\)--------")
p = re.compile("[a-zA-Z]")
print(p.match("apple"))
print(p.match("banana"))
print(p.match("melon"))
print(p.match("Pelon"))

print("--------------")
# . 문자
p = re.compile("a.b")
print(p.match("aab"))   # aab
print(p.match("a0b"))   # a0b
print(p.match("abc"))   # None
print(p.match("a\tb"))  # a\tb
print(p.match("a\nb"))  # None

p = re.compile("a[.]b")
print(p.match("aab"))   # None
print(p.match("a.b"))   # a.b

print("--------------")
p = re.compile("c*")
print(p.match("ctdddddd"))
print(p.match("ccaacaaaaaaaaat"))


p = re.compile("ca*t")
print(p.match("ct"))
print(p.match("caaaaaaaaaaat"))
print(p.match("caaaaaatttaaaaat"))

print("--------------")
p = re.compile("ca+t")
print(p.match("ct"))
print(p.match("cat"))
print(p.match("caat"))
print(p.match("caaaaaaaaaaat"))

print("--------------")
p = re.compile("ca{2,5}t")
print(p.match("ct"))        # None
print(p.match("cat"))       # None
print(p.match("caat"))      # caat
print(p.match("caaaaaaaaaaat")) # None

print("--------------")
p = re.compile("ca{2,}t")
print(p.match("ct"))        # None
print(p.match("cat"))       # None
print(p.match("caat"))      # caat
print(p.match("caaaaaaaaaaat")) # caaaaaaaaaaat

print("--------------")
p = re.compile("ca{,1}t")
print(p.match("ct"))        # ct
print(p.match("cat"))       # cat
print(p.match("caat"))      # None
print(p.match("caaaaaaaaaaat")) # None

print("--------------")
p = re.compile("ca?t")
print(p.match("ct"))        # ct
print(p.match("cat"))       # cat
print(p.match("caat"))      # None
print(p.match("caaaaaaaaaaat")) # None

print("--------------")
# ^ 문자
p = re.compile("^hello")
print(p.match("hello world!"))    # hello
print(p.match(" hello world!"))   # None
print(p.match("\nhello world!"))  # None
print(p.match("pello world!"))    # None

print("------------")

# $ 문자
p = re.compile("world$")
print(p.match("hello world!"))    # None
print(p.match("hello world "))    # None
print(p.match("hello world\n"))   # None
print(p.match("hello world"))     # None
print(p.match("world"))           # world

# p.match() : 문자열의 시작 부분부터 패턴과 일치하는지 확인
# 즉, $를 사용해도 문자열 끝을 찾을 수 없음

print(p.search("hello world!"))   # None
print(p.search("hello world "))   # None
print(p.search("hello world\n"))  # world
print(p.search("hello world"))    # world

# p.search() : 문자열의 전체를 검색하여 패턴 일치하는지 확인
# $는 search()와 함께 사용하는 것이 일반적!

p = re.compile("^hello world$")
print(p.match("hello world"))           # hello world
print(p.match("pello world "))          # None
print(p.match("hello world!"))          # None
print(p.match("hello python world"))    # None