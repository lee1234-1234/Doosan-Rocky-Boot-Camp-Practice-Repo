class Human:
    eyes = 2
    nose = 1
    mouth = 1
    
    def __init__(self, age, name):
        # 인스턴스 변수
        self.age = age
        self.name = name
    
    def intro(self):
        print(str(self.age) + "살", end = " ")
        print(self.name + "입니다.")
        
    def sleep(self):
        print("자다")
        
    def talk(self):
        print("말하다")
    
    def eat(self, food):
        self.food = food
        print(self.food + " 먹다")
        
        
print("눈 개수:", Human.eyes)
print("코 개수:", Human.nose)
print("입 개수:", Human.mouth)

kim = Human(29, "김동건")
kim.intro()
kim.eat("피자")
kim.sleep()


lee = Human(45, "이승우")
lee.intro()
lee.eat("스파게티")



na = "10"
na = int("10")
print(type(na))

# class int():
#     def __init__(self, data):
#         self.data = data
#         #기능: 정수형으로 변환