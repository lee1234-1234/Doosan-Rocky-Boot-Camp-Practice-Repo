class Singer:
    # name = "아이유"
    job = "가수"    # 클래스 멤버 변수

    def call_name(self, name):
        self.name = name    # 인스턴스 멤버 변수
        # print(self.name)
        
    def sing(self):
        print("아아아아dkdkdkdkdkdkdkdk아아아아아아아아아아")
        
print(Singer.job)   # 클래스 변수 사용
iu = Singer()       # 생성자 함수
print(iu.name)      # 속성 확인
print(iu.job)       # 속성 확인
iu.sing()           # 기능 확인
iu.call_name("아이유")
print(iu.name)      # 인스턴스 변수 사용

bts = Singer()
print(bts.job)
bts.call_name("BTS")
print(bts.name)