# phone = Phone("010-1234-5678", "검정")
# print(phone.number)
# print(phone.color)
# 실행결과: 
# 010-1234-5678
# 검정


class Phone:
    def __init__(self, number, color):
        self.number = number
        self.color = color


class SmartPhone(Phone):
    pass
    
phone = Phone("010-1234-5678", "검정")
print(phone.number)
print(phone.color)
