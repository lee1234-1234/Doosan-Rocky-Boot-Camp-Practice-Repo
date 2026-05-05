# 6. 리스트를 이용하여 기본적인 스택(stack)을 구현하세요. (다음 내용을 고려할 것.)
# push(x): 정수 x를 스택에 삽입
# pop(): 스택에서 가장 위의 값을 제거하고 반환. 만약 스택이 비어 있다면 -1을 반환
# top(): 스택의 가장 위에 있는 값을 반환. 만약 스택이 비어 있다면 -1을 반환
# is_empty(): 스택이 비어 있으면 True, 아니면 False를 반환


class Stack:
    # 1. 멤버 변수
    # 1-1. 스택 데이터를 저장할 리스트
    def __init__(self):
        self.stack = []
    
    # 2. 메서드
    # 2-1. push
    # 기능: 스택에 정수 데이터 넣기
    # 입력: 정수 데이터
    # 출력: X
    def push(self, data):
        self.stack.append(data)
        
    # 2-2. pop
    # 기능: 스택의 최상위 데이터를 제거하고 반환
    # 입력: X
    # 출력: 스택의 최상위 데이터, 비어 있으면 -1
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return -1
    
    # 2-3. is_empty
    # 기능: 스택이 비어 있는지 확인
    # 입력: X
    # 출력: 비어 있으면 True, 아니면 False
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    # 2-4. top
    # 기능: 스택의 최상위 데이터 확인
    # 입력: X
    # 출력: 스택의 최상위 데이터, 비어 있으면 -1
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return -1
    
    # 2-5. status_stack
    # 기능: 현재 스택 전체 상태 확인
    # 입력: X
    # 출력: 현재 스택 리스트
    def status_stack(self):
        return self.stack