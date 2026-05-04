# deque_module.py

from collections import deque

dq = deque()        # 덱 생성
print(type(dq))

dq.append(1)         # 뒤로 삽입
print(dq)

dq.appendleft(2)     # 앞으로 삽입
print(dq)

dq.pop()            # 마지막 데이터 제거
print(dq)
if not dq:
    print("비어있음")

dq.popleft()        # 처음 데이터 제거
print(dq)
if not dq:
    print("비어있음")


# 초기값 설정
dq2 = deque([1, 2, 3, 4])
dq2.rotate(1)
print(dq2)
dq2.rotate(-1)
print(dq2)