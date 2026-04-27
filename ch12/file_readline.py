# file_readline.py
# 파일객체명.readline()

# f = open(r"ch12\file.txt", "r")
f = open(r"ch12\file.txt", "r", encoding="utf-8")

line1 = f.readline(5)
line2 = f.readline()
line3 = f.readline()

print(line1)
print(line2)
print(line3)

f.close()