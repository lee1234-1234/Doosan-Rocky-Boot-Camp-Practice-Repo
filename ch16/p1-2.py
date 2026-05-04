# p1-2.py

# 문제 2. 브라우저 뒤로가기 시스템
# 웹 브라우저 방문 기록을 관리하는 프로그램을 작성하세요.
# (앞서 학습한 2가지 자료구조 중 하나를 선택 할 것.)

from stack_class import Stack
browser = Stack()
browser.push("NAVER")
browser.push("YouTube")
browser.push("Google")
print(browser.status_stack())
print(browser.pop())
print(browser.peak())
print(browser.status_stack())