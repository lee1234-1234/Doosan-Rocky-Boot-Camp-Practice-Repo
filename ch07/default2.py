def persona(width, height):
    print("함수 기본값 없음")
    print("width=", width, end=" ")
    print("height=", height)
    
def  persona():
    print("매개변수 없는 함수")

def personb(width=4, height=3):
    print("함수 기본값 있음")
    print("width=", width, end=" ")
    print("height=", height)
    
persona()
personb()
personb(50, 60)