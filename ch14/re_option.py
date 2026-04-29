import re

# DOTALL, S
# p = re.compile("a.b", re.DOTALL)
p = re.compile("a.b", re.S)
print(p.match("a\nb"))  # None => 'a\nb'

print("------------")
# IGNORECASE
p = re.compile("[a-z]+", re.IGNORECASE)
p = re.compile("[a-z]+", re.I)
print(p.match("a\nb"))  # None => 'a\nb'

print("------------")
# MULTILINE
# p = re.compile("^python\s\w+", re.MULTILINE)
p = re.compile("^python\s\w+", re.M)
# p = re.compile("^python\s\w+")
# p = re.complie("\w+\sthree$", re.M)

data = """python one
lise is too short
python two 
you need python 
python three"""

print(p.findall(data))

print("---------------")
# re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

p= re.compile(r"""
• &[#] # Start of a numeric entity reference
• (
• 0[0-7]+ # Octal form(8진수 형식)
• | [0-9]+ # Decimal form(10진수 형식)
• | x[0-9a-fA-F]+ # Hexadecimal form(16진수 형식)
• )
• ; # 후행 semicolon
• """, re.VERBOSE)