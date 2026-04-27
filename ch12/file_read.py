# file_read.py
# 파일객체명.read()

path = r"ch12\file.txt"
f = open(path, "r", encoding="utf-8")

data = f.read()
print(data)

f.close()