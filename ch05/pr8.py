price = 0
while price != -1:
    price = int(input('가격을 입력하세요 (종료:-1): '))
    if price > 10000:
        print('너무 비싸요')
    elif price > 5000:
        print('괜찮은 가격이네요.')
    elif price > 0:
        print('정말 싸요.')