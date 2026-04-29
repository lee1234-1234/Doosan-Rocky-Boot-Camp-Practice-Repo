import re
pattern = r'\w+'
text = "Hello, World!"
print(re.findall(pattern, text))