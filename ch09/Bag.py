# 클래스: 가방
# 객체: 숄더백, 백백, 핸드백, 에코백, 클러치백
# 속성: 재질, 색, 무게, 브랜드, 수납개수, 가격(명사)
# 기능: 넣다, 꺼내다, 꾸미다, 메다, 보호하다

class Bag:
    # 클래스 멤버변수
    call_name = "BAG"
    
    # 맴버함수(메서드)
    def info(self):
        # 인스턴스 멤버변수
        self.kind = ""
        self.color = ""
        self.data = []

    def add(self, x):            # 넣다
        self.data.append(x)
    
    def add_twice(self, x):      # 두번 넣다
        self.add(x)
        self.add(x)
        
    def remove(self, x):
        self.data.remove(x)
        
shoulder = Bag()        # 인스턴스 객체 생성
print(shoulder.call_name)
shoulder.info()
shoulder.add("돈")
shoulder.add("안경")
shoulder.add_twice("휴대폰")
shoulder.remove("휴대폰")
shoulder.remove("휴대폰")
print(shoulder.data)



handbag = Bag()
print(shoulder.call_name)
handbag.info()
handbag.add("지갑")
handbag.add_twice("책")
print(handbag.data)