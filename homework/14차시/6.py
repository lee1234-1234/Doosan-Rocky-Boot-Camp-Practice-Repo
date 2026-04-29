import re

text = "이메일 목록: test@example.com, hello@world.net, user123@domain.org"
p = re.compile(r"[\w.-]+@[\w.-]+\.\w+")
result = p.findall(text)

print(result)