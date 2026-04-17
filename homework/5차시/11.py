# 11. 앞선 프로그램을 수정하여 홀수와 짝수를 구분하여 리스트에 저장하고 출력 하시오.

num = 1
Jlist = []
Hlist = []

while num <= 30:
    if num % 2 == 0:
        Jlist.append(num)
    else:
        Hlist.append(num)
    num += 1

print("짝수:", Jlist)
print("홀수:", Hlist)