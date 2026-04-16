count = 0
while count < 3:
    # count = count + 1
    count += 1
    if count ==2:
        break
    print(count)


print('--------------')
users = ['kim', 'lee', 'park']

for user in users:
    if user == 'lee':
        print("발견")
        break
    
print('--------------')
while True:
    cmd = input("프롬프트")
    if cmd == "python":
        print("파이썬 프로그램 실행")
    elif cmd == "exit":
        print("터미널 종료")
        break