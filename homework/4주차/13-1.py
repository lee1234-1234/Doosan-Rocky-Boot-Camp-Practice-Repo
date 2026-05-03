while True:
    try:
        num = input("숫자를 입력하세요: ")
        num = int(num)
        print(num ** 2)
        break
    except ValueError:
        print("올바른 숫자를 입력하세요!")