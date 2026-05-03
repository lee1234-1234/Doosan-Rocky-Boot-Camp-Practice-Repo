def mygen(n):
    for i in range(1, n + 1):
        result = i ** 2
        yield result


n = int(input("숫자를 입력하세요: "))

for item in mygen(n):
    print(item)