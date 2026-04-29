import re

text = "I love Python. Java is also popular. Python is great for AI."
p = re.compile(r'[^.]*Python[^.]*')
result = p.findall(text)
result = [sentence.strip() for sentence in result]

print(result)