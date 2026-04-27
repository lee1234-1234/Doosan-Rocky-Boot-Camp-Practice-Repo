path = r"ch12\file\계좌1.txt"
mode = "r"
encoding = "utf-8"

f = open(path, mode, encoding=encoding)
lines = f.readlines()
    
account_list = []
    
for line in lines:
    # 음수 슬라이싱
    # print(line[-14:])
    # account_list.append(line[-14:].strip())
    
    # split() 함수 활용
    lineList = line.split()
    account_list.append(lineList[1])
print(account_list)

# print(account_list)