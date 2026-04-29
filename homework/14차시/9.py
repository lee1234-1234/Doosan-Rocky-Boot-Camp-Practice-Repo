# 9. 문자열에서 숫자만 추출하여 리스트로 반환하세요.
# text = "상품 코드: A123, B456, C789, 가격: 12000원"

import re

text = "상품 코드: A123, B456, C789, 가격: 12000원"
p = re.compile(r'\d+')
result = p.findall(text)

print(result)