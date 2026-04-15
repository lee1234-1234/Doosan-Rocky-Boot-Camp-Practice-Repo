week = ['월', '화', '수', '목', '금', '토', '일']
print(week)
print(week[2:5])

#Q1. 토/일 데이터 출력
print(week[5:7])
print(week[5:])

#Q2. 월~목 데이터 출력
print(week[0:4])

print("음수 인덱싱-----------")
print(week[-1])
print(week[-2])
print(week[-3])

print("음수 슬라이싱-----------")
print(week[-3:-1])
print(week[-5:5])

print(week[-1:-3])
print(week[7:5]) #

print(week[-3:6]) #금토
print(week[-3:-1]) #금토

# 시작 인덱스
print(week[:5]) #월화수목금

# 끝 인덱스
print(week[-3:]) #금토일

# 모든 인덱스 생략
print(week[:]) #월화수목금토일
