#사람 함수 만들기
# 데이터는 몸무게, 키, 나이
# 동작사항
# 반환값 없음

#3. 기본값이 있더라도 인수를 설정 가능(인수 우선 처리)
def person_lee(weight = 75, height = 180, age = 25):
    print("체중:", weight, end=" ")
    print("신장:", height, end=" ")
    print("나이:", age)
    
person_lee(80, 150, 28)