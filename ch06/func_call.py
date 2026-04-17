#절대값 구하기

def myabs(arg):
    if (arg < 0):
        result = arg * -1
    else:
        result = arg
    return result

print(myabs(10))


print('---------------')
def funca():
    print('a 함수 호출')

def funcb():
    funca()
    print('b 함수 호출')

def funcc():
    funcb()
    print('c 함수 호출')
    
funcc()