def persona(width = 11, height = 21):
    print("함수 기본값 없음")
    print("width=", width, end=" ")
    print("height=", height)
    

def personb(width=4, height=3):
    print("함수 기본값 있음")
    print("width=", width, end=" ")
    print("height=", height)
    
persona(10, 20)
persona()
personb()

personb(10)