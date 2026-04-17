# 함수 정의

def my_func():
    print('토끼야 안녕!')
    print('거북아 안녕!')
    print('사자야 안녕!')
    print('코끼리야 안녕!')

my_func()
my_func()


print("-------------")
def fhello():
    print("매개변수 없는 함수 호출")

fhello()

print("--------------")
def  funca(na, nb):
    nc = na + nb
    print(na, "+", nb, "=", nc)
    
funca(10, 20)
funca(1, 2)

print("--------------")
def add(num1, num2):
    return num1 + num2

print(add(2, 3))


print("--------------")
def sub(num1, num2):
    return num1 - num2

print(sub(4, 2))