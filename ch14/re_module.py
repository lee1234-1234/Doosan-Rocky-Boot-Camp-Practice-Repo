# re_moudule.py

import re
p = re.compile("[a-z]+")    # 한 번 이상 반복할 때
m = p.match("python")     # python
# m = p.match("3 python")     # None
# print(m)

if m:
    print("Match found:", m.group())
else:
    print('No match')