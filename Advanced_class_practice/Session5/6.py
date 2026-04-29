import time

def log_decorator(func):
    def wrapper():
        print(f"[LOG] {func.__name__} 함수가 실행되었습니다.")
        func()
    return wrapper

def time_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"실행 시간: {end - start:.6f}초")
    return wrapper

@log_decorator
@time_decorator
def search_book():
    for i in range(1000000):
        pass  # 프로젝트 예제에서는 실제 검색 코드를 사용하면 됩니다.
    print("도서 검색 완료")

search_book()