# 10. 주어진 문자열에서 연속된 대문자(예: NASA, AI)만 찾아 리스트로 반환하세요.
# text = "NASA is working on AI projects with IBM and Google."

import re

text = "NASA is working on AI projects with IBM and Google."
p = re.compile(r'[A-Z]{2,}')
result = p.findall(text)

print(result)