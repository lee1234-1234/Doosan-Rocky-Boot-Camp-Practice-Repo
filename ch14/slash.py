# slash.py

import re
# 패턴 객체 = re.compile("장규표현식")
# 패턴 객체.match("대상문자열")

# "\section"문자열 검색

# p = re.compile("\section")      # None
# p = re.compile("\\section")     # None
# p = re.compile("\\\\section")   # match='\\section
p = re.compile(r"\\section")      # match='\\section
print(p.match('\section python hello thanks'))

# 1.파이썬 리터럴 규칙(이스케이프)
# "\\" => "\"
# "\\\\" => "\\"
# 2. '\s' 정규표현식 화이트스페이스 의미
# \\section

# raw string
# => 파이썬 문자열 리터럴 안에서
# \n, \t 같은 "이스케이프 코드 처리"를 없애주는 역할