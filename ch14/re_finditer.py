# re_findall.py

import re
p = re.compile("[a-z]+")    # 한 번 이상 반복할 때
results = p.finditer("life is too short")     # py
print(results)        # ['life', 'is', 'too', 'short']

results = p.finditer("3 py8thon")
print(results)        # ['py', 'thon']
    
print("----------------")
p = re.compile("Python")
results = p.finditer("The mission of the Python Software Foundation is Python and Python and Python or Python")
print(results)    # ['Python', 'Python', 'Python', 'Python', 'Python']

print("----------------")
for m in results:
    print(m)        # match object
    print("매치 문자열:", m.group())
    print("문자열 위치:", m.span())
    print("시작 위치:", m.start())
    print("끝 위치:", m.end())
