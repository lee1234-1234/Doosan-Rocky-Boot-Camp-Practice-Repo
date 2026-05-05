# 8. 리스트를 사용하여 기본적인 큐(queue)를 구현하세요. (다음 내용을 고려할 것.)
# enqueue(x): 정수 x를 큐의 끝에 추가
# dequeue(): 큐의 앞에서 값을 제거하고 반환. 만약 큐가 비어 있다면 -1을 반환
# front(): 큐의 앞에 있는 값을 반환. 만약 큐가 비어 있다면 -1을 반환
# is_empty(): 큐가 비어 있으면 True, 아니면 False를 반환

class Queue:
    # 0. 큐 리스트 생성 = 데이터 공간 초기화
    def __init__(self):
        self.queue = []
        
    # 1. Enqueue: 데이터 삽입
    def enqueue(self, data):
        self.queue.append(data)
    
    # 2. Dequeue: 데이터 제거
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return -1
    
    # 3. Front
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return -1
            
    # 4. 큐가 비어있는지 확인
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False
    
    # 5. 큐 상태 반환
    def status_queue(self):
        return self.queue