class Human:
    # 1. 맴버 변수
    eyes = 2        # 클래스 변수
    nose = 1
    mouth = 1
    
    # 2. 맴버 함수(매서드)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("이름: ", self.name)     # 인스턴스 변수
        print("나이: ", self.age)
    def eat(self):
        print("먹다")
    def sleep(self):
        print("자다")
    def talk(self):
        print("말하다")
    
class Student(Human):
    def __init__(self, name, age, studentNum):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        self.studentNum = studentNum
    def introduce(self):
        # print("이름: ", self.name)     # 인스턴스 변수
        # print("나이: ", self.age)
        super().introduce()
        print("학번: ", self.studentNum)
    def study(self):
        print("공부하다")
        
print("-----------------")
print("눈 개수: ", Human.eyes)  # 클래스 변수 접근
lee = Human("이수근", 48)       # 객체 생성 및 초기 데이터 설정
print(lee.name)                 #인스턴스 변수 접근
print(lee.age)
lee.introduce()                 # 매서드 접근
lee.eat()
lee.sleep()

print("----------------")
print("눈 개수: ", Human.eyes)   # 부모 속성 데이터 상속
print("코 개수: ", Human.nose)
kim = Student("김수로", 56, 20222222)
print(kim.name)
print(kim.age)
kim.introduce()
kim.eat()               # 부모 기능/동작 상속
kim.study()