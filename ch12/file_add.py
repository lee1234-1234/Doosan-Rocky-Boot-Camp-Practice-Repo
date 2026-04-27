# file_add.py

path = r"ch12\file.txt"
mode = "a"
f = open(path, mode, encoding="utf-8")

for i in range(11, 21):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)

f.close()

mode = "r"
f = open(path, mode, encoding="utf-8")
print(f.read())
f.close