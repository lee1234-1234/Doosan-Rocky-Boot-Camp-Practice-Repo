# 10. 리스트를 이용하여 덱(deque, 양방향 큐)을 구현하세요. (다음 내용을 고려할 것.)
# push_front(x): 정수 x를 덱의 앞에 추가
# push_back(x): 정수 x를 덱의 뒤에 추가
# pop_front(): 덱의 앞에서 값을 제거하고 반환 (비어 있다면 -1)
# pop_back(): 덱의 뒤에서 값을 제거하고 반환 (비어 있다면 -1)

class deque:
    def __init__(self):
        self.deque = []
    
    def push_front(self, data):
        self.deque.insert(0, data)
    
    def push_back(self, data):
        self.deque.append(data)
    
    def pop_front(self):
        if not self.is_empty():
            return self.deque.pop(0)
        return -1

    def pop_back(self):
        if not self.is_empty():
            return self.deque.pop()
        return -1
    
    def is_empty(self):
        if len(self.deque) == 0:
            return True
        return False
    
dq = deque()
dq.push_front(10)
print(dq.deque)

dq.push_front(11)
print(dq.deque)

dq.push_front(12)
print(dq.deque)

dq.push_back(13)
print(dq.deque)

dq.pop_back()
print(dq.deque)

dq.pop_front()
print(dq.deque)