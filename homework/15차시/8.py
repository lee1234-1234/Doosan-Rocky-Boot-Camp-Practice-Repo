# 8. 0부터 9까지의 숫자를 이터레이터로 순회하며, 
# 각 숫자의 제곱을 출력하는 프로그램을 작성하세요.

nums = iter(range(10))

for n in nums:
    print(n**2)