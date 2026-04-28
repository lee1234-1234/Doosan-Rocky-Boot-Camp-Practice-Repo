# 사용 예
# 잘못된 값 들어왔을 때 방지
# 함수에서 조건을 위반 시 실행 중단
# 사용자 정의 에어 처리

# 예) 은행 잔고 부족시 예외 발생
class insufficientValanceError(Exception):
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise insufficientValanceError("잔고가 부족합니다.")
        self.balance -= amount
        return self.balance

lim = Account(1000)
lim.withdraw(2000)