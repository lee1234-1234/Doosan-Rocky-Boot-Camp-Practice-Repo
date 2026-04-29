def log_decorator(func):
    def wrapper():
        print(f"[LOG] {func.__name__} 함수가 실행되었습니다.")
        func()
    return wrapper

@log_decorator
def borrow_book():
    print("책을 대여합니다.")
    
@log_decorator
def return_book():
    print("책을 반납합니다.")
    
borrow_book()
return_book()