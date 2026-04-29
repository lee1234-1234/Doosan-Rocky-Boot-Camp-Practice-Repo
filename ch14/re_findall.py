# re_findall.py

import re
p = re.compile("[a-z]+")    # 한 번 이상 반복할 때
m = p.findall("life is too short")     # py
print(m)        # ['life', 'is', 'too', 'short']

m = p.findall("3 py8thon")
print(m)        # ['py', 'thon']
    
print("----------------")
p = re.compile("Python")
m = p.findall("The mission of the Python Software Foundation is Python and Python and Python or Python")
print(m)    # ['Python', 'Python', 'Python', 'Python', 'Python']
