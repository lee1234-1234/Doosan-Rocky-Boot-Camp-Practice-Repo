import time
def time_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"실행 시간: {end - start:.6f}초")
    return wrapper
    
@time_decorator
def borrow_book():
    print("책을 대여합니다.")
    
@time_decorator
def return_book():
    print("책을 반납합니다.")
    
borrow_book()
return_book()