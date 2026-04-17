def fdiv(num1, num2):
    if num2 == 0:
        return("0으로는 나눌 수 없다.")
    else:
        return num1 / num2

num1 = int(input("숫자를 입력: "))
num2 = int(input("숫자를 입력: "))

print(fdiv(num1, num2))