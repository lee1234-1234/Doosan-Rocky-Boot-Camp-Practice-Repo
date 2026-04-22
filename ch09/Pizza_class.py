# class 클래스명:
#     # 1.멤버변수
#     변수명 = 속성값
    
#     # 2.멤버함수(메서드)
#     def 함수명(self, 매개변수):
#         self.멤버변수 = 속성값
#         return 반환값
    
    
# # 빈 클래스
# class 클래스명:
#     pass        #일단 pass 할게요. 아직 뭐 넣을지 몰라요~

class Pizzclass:
    def order(self):
        print("주문하다.")
        self.kind = 10

# 객체 생성(클래스 사용)
na = Pizzclass()

na.order()
print(na.kind)





# class Singer:
#     name = "아이유"
#     def sing(self):
#         print("아아아아")
        
# iu = Singer()
# print(iu.name)
# iu.sing()