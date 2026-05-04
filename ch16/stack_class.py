# stack_class

# class 클래스명:
#     # 1. 멤버 변수
#     # 1-1. 스택 리스트
    
#     # 2. 메서드
#     # 2-1. push
#     # 2-2. pop
#     # 2-3. 스택 내 데이터 유무 확인
#     # 2-4. 스택 최상위(Top) 데이터 확인
#     # 2-5. 스택 상태 반환
#     pass




class Stack:
    # 1. 멤버 변수
    # 1-1. 스택 리스트
    def __init__(self):
        self.stack = []
    
    # 2. 메서드
    # 2-1. push
    # 기능: 스택에 데이터 넣기
    # 입력: 데이터
    # 출력: X
    def push(self, data):   # 입력데이터 있으니까 매개변수 data 넣음
        self.stack.append(data)
        
    # 2-2. pop
    # 기능: 스택에 데이터 제거
    # 입력: X
    # 출력: 스택 내 상단 데이터
    def pop(self):
        # 스택이 비어있는 경우 고려
        if not self.is_empty():
            return self.stack.pop() # 상단 데이터 꺼내고 return까지
        return
    
    # 2-3. 스택 내 데이터 유무 확인
    # 리스트가 빈 리스트인지 or 길이를 통해 유무 확인
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    # 2-4. 스택 최상위(Top) 데이터 확인
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        return
    
    # 2-5. 스택 상태 반환
    def status_stack(self):
        return self.stack

if __name__ == "__main__":
    s1 = Stack()
    print(s1.peak)
    s1.pop()
    print(s1.status_stack())
    s1.push(1)
    print(s1.status_stack())
    s1.push(2)
    print(s1.status_stack())
    s1.pop()
    print(s1.status_stack())
    s1.push(3)
    print(s1.status_stack())
    s1.push(4)
    print(s1.status_stack())
    print(s1.peak)