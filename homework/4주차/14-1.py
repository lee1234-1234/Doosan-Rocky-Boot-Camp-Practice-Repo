import re

data = """python one
life is too short
python two
you need python
python three"""

p = re.compile("^python.*", re.MULTILINE)

m = p.findall(data)

print(m)
