def fadd(num1, num2):
    return num1 + num2

def fsub(num1, num2):
    return num1 - num2

def fmul(num1, num2):
    return num1 * num2

def fdiv(num1, num2):
    return num1 / num2

num1 = int(input("숫자를 입력: "))
num2 = int(input("숫자를 입력: "))

print(fadd(num1, num2))
print(fsub(num1, num2))
print(fmul(num1, num2))
print(fdiv(num1, num2))