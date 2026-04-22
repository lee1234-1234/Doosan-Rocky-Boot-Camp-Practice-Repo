# 클래스: 객체들
# 가수: 아이유, BTS
# 속성(데이터, 명사)
# 기능(동작, 동사): 함수 => 노래부르다

# class Singer:
#     맴버변수 = 속성값
#     def 함수명(self):
#         코드블록

class Singer:
    name = "아이유"
    def sing(self):
        print("아아아아")
        

iu = Singer()   # 생성자 함수

print(iu.name)  # 속성 확인
iu.sing()       # 기능 확인
