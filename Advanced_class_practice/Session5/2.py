def write_log(func_name):
    print(f"[LOG] {func_name} 함수가 실행되었습니다.")
    
def borrow_book():
    write_log("borrow_book")
    print("책을 대여합니다.")
    
borrow_book()