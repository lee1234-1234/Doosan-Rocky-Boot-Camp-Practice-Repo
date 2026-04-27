# file_readlines.py
# 파일객체명.readlines()

path = r"ch12\file.txt"
f = open(path, "r", encoding="utf-8")

lines = f.readlines()
print(type(lines))

for line in lines:
    print(line, end="")

f.close()