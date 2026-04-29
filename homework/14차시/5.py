import re
pattern = r'(ab)+'
text = "ababab"
match = re.match(pattern, text)
print(match.group())
