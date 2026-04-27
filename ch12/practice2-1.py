path = r"ch12\file\계좌1.txt"
mode = "r"
encoding = "utf-8"

account_list = []

with open(path, mode, encoding=encoding) as file:
    lines = file.readlines()
    
    for line in lines:
        name, account = line.strip().split()
        account_list.append(account)

print(account_list)