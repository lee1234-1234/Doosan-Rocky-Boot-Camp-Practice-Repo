b = 0
print("b의 값은", b)
b = 1
print("b의 값은", b)

def scope_test():
    global a
    a = 1
    print("함수 내 a 값:", a)
    
a = 0
print("함수 밖 a 값:", a)
scope_test()
print("함수 호출 후 a 값:", a)