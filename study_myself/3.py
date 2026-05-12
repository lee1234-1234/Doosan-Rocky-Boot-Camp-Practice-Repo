def fplusminus(arg):
    if arg > 0:
        return "plus"
    elif arg < 0:
        return "minus"
stra = fplusminus(0) # 인수가 0인 경우 반환할 값이 없음
print(stra) # 이 경우 함수는 호출자에게 None 을 반환
