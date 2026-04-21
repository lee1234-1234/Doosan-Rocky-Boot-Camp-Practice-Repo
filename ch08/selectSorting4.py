ca = [21, 10, 11, 15, 13]
print(ca)

print("--------------------")

# 0번 위치에 들어갈 가장 작은 값을 찾기
mina = ca[0]      # 현재 최솟값
minix = 0         # 현재 최솟값의 인덱스

for sb in range(1, 5, 1):   # 1, 2, 3, 4 검사
    if mina > ca[sb]:       # 더 작은 값이 나오면
        mina = ca[sb]       # 최솟값 갱신
        minix = sb          # 최솟값 위치 갱신

# 0번 값과 최솟값 위치의 값을 교환
temp = ca[0]
ca[0] = ca[minix]
ca[minix] = temp
print(ca)
# 1차 목표: [10, 21, 11, 15, 13]

print("--------------------")

# 1번 위치에 들어갈 가장 작은 값을 찾기
mina = ca[1]
minix = 1

for sb in range(2, 5, 1):   # 2, 3, 4 검사
    if mina > ca[sb]:       # 예: 21 > 11 이면 True
        mina = ca[sb]       # mina = 11
        minix = sb          # minix = 2

# 1번 값과 최솟값 위치의 값을 교환
temp = ca[1]
ca[1] = ca[minix]
ca[minix] = temp
print(ca)
# 2차 목표: [10, 11, 21, 15, 13]

print("--------------------")

# 2번 위치에 들어갈 가장 작은 값을 찾기
mina = ca[2]
minix = 2

for sb in range(3, 5, 1):   # 3, 4 검사
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb

# 2번 값과 최솟값 위치의 값을 교환
temp = ca[2]
ca[2] = ca[minix]
ca[minix] = temp
print(ca)
# 3차 목표: [10, 11, 13, 15, 21]

print("--------------------")

# 3번 위치에 들어갈 가장 작은 값을 찾기
mina = ca[3]
minix = 3

for sb in range(4, 5, 1):   # 4만 검사
    if mina > ca[sb]:       # 15 > 21 이므로 False
        mina = ca[sb]       # 실행되지 않음
        minix = sb          # 실행되지 않음

# 이미 3번 위치가 더 작으므로 그대로 둠
temp = ca[3]
ca[3] = ca[minix]
ca[minix] = temp
print(ca)
# 4차 목표: [10, 11, 13, 15, 21]