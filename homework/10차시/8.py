# 8. 다음 코드가 동작하도록 핸드폰 (Phone) 클래스를 수정하세요.
# phone = Phone("010-1234-5678", "검정")
# phone.showInfo()
# 실행결과:
# 전화번호: 010-1234-5678
# 색상: 검정

class Phone:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        
    def showInfo(self):
        print("전화번호:", self.number)
        print("색상:", self.color)
        
class SmartPhone(Phone):
    def __init__(self, number, color, company):
        super().__init__(number, color)
        self.company = company

    
phone = Phone("010-1234-5678", "검정")
phone.showInfo()