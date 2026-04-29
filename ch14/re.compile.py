import re

# 축약 전 형태
p = re.compile("[a-z]+")
m = p.match("python")

print()
# 축약 후 형태
# 매치객체 = re.match("정규식", "검색대상문자열")