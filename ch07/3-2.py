#사람 함수 만들기
# 데이터는 몸무게, 키, 나이
# 동작사항
# 반환값 없음

#2. 인수 전달 시 앞에서부터 설정 가능
def person_lee(weight = 75, height = 180, age = 25):
    print("체중:", weight, end=" ")
    print("신장:", height, end=" ")
    print("나이:", age)
    
person_lee(75)
person_lee(75, 180)