# 9. 0부터 10까지의 숫자 중 짝수만 출력하는 프로그램을 작성하세요. 
# 이때, 이터레이터를 사용해야 합니다.


nums = iter(range(11))

for n in nums:
    if n%2 == 0:
        print(n)