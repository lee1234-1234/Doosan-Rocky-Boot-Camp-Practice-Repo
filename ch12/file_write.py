# 파일객체명.write(data)

f = open(r"ch12\file.txt", "w", encoding="utf-8")

# f.write("hi")


for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
    
f.close()