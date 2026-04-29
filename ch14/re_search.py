# re_search.py

import re
p = re.compile("[a-z]+")    # 한 번 이상 반복할 때
# m = p.search("python")     # python
# m = p.search("3 python")     # python
m = p.search("3 py8thon")     # py
# print(m)

if m:
    print("Match found:", m.group())
    print("위치:", m.span())
else:
    print("No match")
    
    
print("----------------")
p = re.compile("Python")
m = p.search("The mission of the Python Software Foundation is Good")
print(m)