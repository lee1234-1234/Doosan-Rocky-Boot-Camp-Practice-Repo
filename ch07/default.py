def persona(width, height):
    print("함수 기본값 없음")
    print("width=", width, end=" ")
    print("height=", height)
    
def personb(width=4, height=3):
    print("함수 기본값 없음")
    print("width=", width, end=" ")
    print("height=", height)
    
persona(10, 20)
persona(30, 40)
personb()
personb(50, 60)