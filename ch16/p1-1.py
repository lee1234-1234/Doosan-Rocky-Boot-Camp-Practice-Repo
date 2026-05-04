# p1-1.py

# 문제 1. 은행 번호표 시스템
# 은행에서 고객 상담을 위해 번호표 대기 시스템을 만들려고 합니다. 
# (앞서 학습한 2가지 자료구조 중 하나를 선택 할 것.)


# 번호표 => 철수 => 영희 => 민수
from queue_class import Queue
bank = Queue()
bank.enqueue("철수")
bank.enqueue("영희")
bank.enqueue("민수")
print(bank.status_queue())
print(bank.dequeue())       # 첫번째 상담자
print(bank.status_queue())


# class BankQueue:
#     def __init__(self):
#         self.queue = []
    
#     def enqueue(self, data):
#         self.queue.append(data)
    
#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.pop(0)
#         return
    
#     def is_empty(self):
#         if len(self.queue) == 0:
#             return True
#         return False
    
#     def queue_status(self):
#         return self.queue