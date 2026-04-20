#사람 함수 만들기
# 데이터는 몸무게, 키, 나이
# 동작사항
# 반환값 없음

#1. 모든 매개변수에 기본값 설정 가능
def person_lee(weight = 75, height = 180, age = 25):
    print("체중:", weight, end=" ")
    print("신장:", height, end=" ")
    print("나이:", age)
    
person_lee()