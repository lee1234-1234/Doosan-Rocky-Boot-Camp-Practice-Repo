path = r"ch12\file3.txt"
mode = "w+"
f = open(path, mode, encoding='utf-8')

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
    
f.seek(0)   # 파일 포인터 위치 재조정
print(f.read())

f.close()