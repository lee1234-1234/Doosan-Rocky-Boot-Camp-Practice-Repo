# 9. 앞서 작성한 큐 클래스를 활용하여 은행에 도착한 고객 순서대로 업무를 처리하는 선입선출(FIFO) 구조의 큐 프로그램을 작성하세요. 리스트를 활용하여 아래 기능을 수행하는 코드를 작성하세요. (다음 조건을 고려할 것.)
# 조건:
# 1. 고객이 도착하면 이름을 큐에 추가합니다 (Enqueue). 
# 2. 업무 처리가 시작되면 가장 먼저 온 고객부터 이름을 출력하고 큐에서 제거합니다 (Dequeue). 
# 3. 현재 대기 중인 고객 명단을 확인하는 기능을 포함하세요.

# 실행 결과 예시)
# 현재 대기열: ['김철수', '이영희', '박민수']   
# 업무 처리 중인 고객: 김철수
# 남은 대기 고객: ['이영희', '박민수']

from queue8 import Queue

bank = Queue()
bank.enqueue("김철수")
bank.enqueue("이영희")
bank.enqueue("박민수")

print("현재 대기열:", bank.status_queue())
customer = bank.dequeue()
print("업무 처리 중인 고객:", customer)
print("남은 대기 고객:", bank.status_queue())