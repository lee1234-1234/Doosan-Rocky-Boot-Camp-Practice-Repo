# queue_class.py

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
        return
        
    # 3. 큐가 비어있는지 확인
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False
    
    # 4. 큐 상태 반환
    def status_queue(self):
        return self.queue
    
if __name__ == "__main__":
    q1 = Queue()    # 큐 생성
    q1.dequeue()
    print(f"Queue: {q1.status_queue()}")
    q1.enqueue(1)
    q1.enqueue(2)
    print(f"Queue: {q1.status_queue()}")
    q1.dequeue()
    q1.dequeue()
    q1.enqueue(3)
    print(f"Queue: {q1.status_queue()}")
    q1.dequeue()
    q1.enqueue(4)
    print(f"Queue: {q1.status_queue()}")