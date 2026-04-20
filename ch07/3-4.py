#사람 함수 만들기
# 데이터는 몸무게, 키, 나이
# 동작사항
# 반환값 없음

#4. 부분 매개변수에 기본값 설정시 뒤에서 부터 설정할 것
def person_lee(weight, height = 180, age = 25):
    print("체중:", weight, end=" ")
    print("신장:", height, end=" ")
    print("나이:", age, end=" ")
    
person_lee(55)