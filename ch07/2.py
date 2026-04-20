def persona(width, height):
    print("함수디폴트값없음, width=", width, "height=", height)
    
def personb(width=4, height=3):
    print("함수디폴트값없음width=", width, "height=", height)
    
persona(10, 20)
persona()
personb()