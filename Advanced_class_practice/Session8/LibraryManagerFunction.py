# -*- coding: utf-8 -*-
"""
LibraryManagerFunction.py

도서 대여/반납 기능과 리포트 기능을 담당하는 파일입니다.
GUI 파일(LibraryManagerGUI.py)과 분리해서 사용합니다.
"""

import csv
import datetime
import time


class LogConfig:
    # "DEBUG": 상세 로그 출력
    # "INFO": 시간 등 필수 로그만 출력
    # "NONE": 로그 출력 안 함
    LEVEL = "NONE"
    FILE_LEVEL = "DEBUG"


def trace_decorator(func):
    def wrapper(self, *args, **kwargs):
        if LogConfig.LEVEL == "DEBUG":
            call_args = ", ".join([str(arg) for arg in args])
            print(f"[DEBUG] '{func.__name__}' 실행 (입력값: {call_args})")

        return func(self, *args, **kwargs)

    return wrapper


def time_decorator(func):
    def wrapper(self, *args, **kwargs):
        start = time.time()
        result = func(self, *args, **kwargs)
        end = time.time()

        if LogConfig.LEVEL in ["DEBUG", "INFO"]:
            print(f"[INFO] ⏱ '{func.__name__}' 소요 시간: {end - start:.6f}초")

        return result

    return wrapper


def log_transaction(action_type):
    def decorator(func):
        def wrapper(self, user_id, book_id, *args, **kwargs):
            result = func(self, user_id, book_id, *args, **kwargs)

            if LogConfig.FILE_LEVEL == "DEBUG":
                today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                log_message = f"{action_type},{user_id},{book_id},{today}\n"

                with open("library_log.txt", "a", encoding="utf-8") as file:
                    file.write(log_message)

            return result

        return wrapper

    return decorator


class BookNotFoundError(Exception):
    def __init__(self, book_id):
        super().__init__(f"없는 책 번호입니다: {book_id}")


class UserNotFoundError(Exception):
    def __init__(self, user_id):
        super().__init__(f"없는 회원 번호입니다: {user_id}")


class BookNotAvailableError(Exception):
    def __init__(self, message="이미 대여 중인 책입니다."):
        super().__init__(message)


class BookNotBorrowedError(Exception):
    def __init__(self, message="이 회원이 대여한 책이 아닙니다."):
        super().__init__(message)


class Book:
    def __init__(self, book_id, title, author, available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True

    def show_info(self):
        status = "대여가능" if self.available else "대여 중"
        print(f"[{self.book_id}] {self.title} / {self.author} / {status}")


class User:
    def __init__(self, user_id, name, phone):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.borrowed_books = []

    def add_book(self, book):
        self.borrowed_books.append(book)

    def remove_book(self, book):
        self.borrowed_books.remove(book)

    def show_info(self):
        print(f"회원번호: {self.user_id}, 이름: {self.name}")
        print("대여중인 책 수:", len(self.borrowed_books))


class LibraryManager:
    def __init__(self):
        self.books = {}
        self.users = {}

    @time_decorator
    @trace_decorator
    def load_books(self, filename):
        try:
            with open(filename, "r", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    book = Book(
                        int(row["book_id"].strip()),
                        row["title"].strip(),
                        row["author"].strip(),
                        row["available"].strip() == "True"
                    )
                    self.books[book.book_id] = book

            print(f"{filename} 파일 로드 완료 (총 {len(self.books)}권)")

        except FileNotFoundError:
            print(f"경고: {filename} 파일이 없어 빈 목록으로 시작합니다.")
        except KeyError as e:
            print(f"CSV 컬럼 오류: {filename} 파일에 {e} 컬럼이 없습니다.")
        except Exception as e:
            print(f"{filename} 파일 로드 중 오류 발생:", e)

    @time_decorator
    @trace_decorator
    def load_users(self, filename):
        try:
            with open(filename, "r", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    user = User(
                        int(row["user_id"].strip()),
                        row["name"].strip(),
                        row["phone"].strip()
                    )
                    self.users[user.user_id] = user

            print(f"{filename} 파일 로드 완료 (총 {len(self.users)}명)")

        except FileNotFoundError:
            print(f"경고: {filename} 파일이 없어 빈 목록으로 시작합니다.")
        except KeyError as e:
            print(f"CSV 컬럼 오류: {filename} 파일에 {e} 컬럼이 없습니다.")
        except Exception as e:
            print(f"{filename} 파일 로드 중 오류 발생:", e)

    @trace_decorator
    def find_book_by_id(self, book_id):
        if book_id in self.books:
            return self.books[book_id]

        raise BookNotFoundError(book_id)

    @trace_decorator
    def find_user_by_id(self, user_id):
        if user_id in self.users:
            return self.users[user_id]

        raise UserNotFoundError(user_id)

    @trace_decorator
    def find_book_ids_by_title(self, keyword):
        found_ids = []

        for book_id, book in self.books.items():
            if keyword in book.title:
                found_ids.append(book_id)

        if not found_ids:
            raise BookNotFoundError(keyword)

        return found_ids

    @time_decorator
    @trace_decorator
    @log_transaction("BORROW")
    def borrow_book(self, user_id, book_id):
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)

        if not book.available:
            raise BookNotAvailableError(
                f"'{book.title}' 책은 이미 대여 중입니다."
            )

        book.borrow()
        user.add_book(book)

        print(f"{user.name} 회원이 '{book.title}' 책을 대여했습니다.")

    @time_decorator
    @trace_decorator
    @log_transaction("RETURN")
    def return_book(self, user_id, book_id):
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)

        if book not in user.borrowed_books:
            raise BookNotBorrowedError(
                f"{user.name} 회원이 대여한 책이 아닙니다: {book.title}"
            )

        book.return_book()
        user.remove_book(book)

        print(f"{user.name} 회원이 '{book.title}' 책을 반납했습니다.")

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_user(self, user):
        self.users[user.user_id] = user


class TestCase:
    def __init__(self, manager, test_user_id=101, sub_user_id=102, keyword="파이썬"):
        self.manager = manager

        self.test_user_id = test_user_id
        self.sub_user_id = sub_user_id
        self.keyword = keyword

        self.book_ids = []
        self.selected_book_id = 1
        self._prepare_data()
        self._reset_test_state()

    def _prepare_data(self):
        if not self.manager.books:
            print("도서 데이터가 부족하여 테스트용 임시 도서를 추가합니다.")
            self.manager.add_book(Book(1, "파이썬 입문", "홍길동", True))
            self.manager.add_book(Book(2, "자료구조 기초", "김영희", True))
            self.manager.add_book(Book(3, "파이썬 실습", "이민수", True))

        if not self.manager.users:
            print("회원 데이터가 부족하여 테스트용 임시 회원을 추가합니다.")
            self.manager.add_user(User(101, "김민수", "1111-2222"))
            self.manager.add_user(User(102, "박영희", "3333-4444"))

    def _reset_test_state(self):
        for book in self.manager.books.values():
            book.available = True

        for user in self.manager.users.values():
            user.borrowed_books.clear()

    def _to_int_id(self, value, label):
        value = str(value).strip()

        if not value:
            raise ValueError(f"{label}를 입력해주세요.")

        try:
            return int(value)
        except ValueError:
            raise ValueError(f"{label}는 숫자로 입력해주세요: {value}")

    def find_user_by_id_for_gui(self, user_id):
        """
        GUI 회원 ID 조회 버튼에서 호출하는 함수입니다.
        정상 조회 시 User 객체를 반환합니다.
        """
        try:
            user_id = self._to_int_id(user_id, "회원 ID")
            user = self.manager.find_user_by_id(user_id)

            self.test_user_id = user.user_id

            print(f"{user.name} 회원님 안녕하세요.")
            return user

        except UserNotFoundError as e:
            print("회원 검색 실패:", e)
        except ValueError as e:
            print("입력 오류:", e)
        except Exception as e:
            print("다른 오류 발생:", e)

        return None

    def find_book_by_id_for_gui(self, book_id):
        """
        GUI 책 ID 조회 버튼에서 호출하는 함수입니다.
        정상 조회 시 Book 객체를 반환합니다.
        """
        try:
            book_id = self._to_int_id(book_id, "책 ID")
            book = self.manager.find_book_by_id(book_id)

            self.selected_book_id = book.book_id

            status = "가능" if book.available else "불가능"
            print(f"{book.title} 도서는 대여{status}합니다.")
            return book

        except BookNotFoundError as e:
            print("검색 실패:", e)
        except ValueError as e:
            print("입력 오류:", e)
        except Exception as e:
            print("다른 오류 발생:", e)

        return None

    def borrow_selected_book_for_gui(self):
        """
        GUI 대여 버튼에서 호출하는 함수입니다.
        현재 선택된 회원 ID와 책 ID로 대여를 시도합니다.
        """
        try:
            self.test_successful_borrow(self.test_user_id, self.selected_book_id)

        except UserNotFoundError as e:
            print("예외 정상 발생 (UserNotFoundError):", e)
        except BookNotFoundError as e:
            print("검색 실패:", e)
        except BookNotAvailableError as e:
            print("대여 실패:", e)
        except BookNotBorrowedError as e:
            print("예외 정상 발생 (BookNotBorrowedError):", e)
        except Exception as e:
            print("다른 오류 발생:", e)

    def return_selected_book_for_gui(self):
        """
        GUI 반납 버튼에서 호출하는 함수입니다.
        현재 선택된 회원 ID와 책 ID로 반납을 시도합니다.
        """
        try:
            self.test_successful_return(self.test_user_id, self.selected_book_id)

        except UserNotFoundError as e:
            print("예외 정상 발생 (UserNotFoundError):", e)
        except BookNotFoundError as e:
            print("검색 실패:", e)
        except BookNotAvailableError as e:
            print("대여 실패:", e)
        except BookNotBorrowedError as e:
            print("예외 정상 발생 (BookNotBorrowedError):", e)
        except Exception as e:
            print("다른 오류 발생:", e)

    def test_successful_borrow(self, test_user_id=101, test_book_id=1):
        print("\n[대여 처리]")

        self.manager.borrow_book(test_user_id, test_book_id)

    def test_successful_return(self, test_user_id=101, test_book_id=1):
        print("\n[반납 처리]")

        self.manager.return_book(test_user_id, test_book_id)

    def test_book_not_found(self):
        print("\n[테스트 3] 없는 책 번호 예외 테스트")

        try:
            self.manager.borrow_book(self.test_user_id, 999)

        except BookNotFoundError as e:
            print("예외 정상 발생 (BookNotFoundError):", e)

        except Exception as e:
            print("다른 오류 발생:", e)

    def test_user_not_found(self):
        print("\n[테스트 4] 없는 회원 번호 예외 테스트")

        try:
            self.manager.find_user_by_id(999)

        except UserNotFoundError as e:
            print("예외 정상 발생 (UserNotFoundError):", e)

        except Exception as e:
            print("다른 오류 발생:", e)

    def test_book_not_available(self):
        print("\n[테스트 5] 이미 대여 중인 책 예외 테스트")

        try:
            self.manager.borrow_book(self.test_user_id, 1)
            self.manager.borrow_book(self.sub_user_id, 1)

        except BookNotAvailableError as e:
            print("예외 정상 발생 (BookNotAvailableError):", e)

        except Exception as e:
            print("다른 오류 발생:", e)

    def test_return_unborrowed_book(self):
        print("\n[테스트 6] 빌리지 않은 책 반납 예외 테스트")

        try:
            self.manager.return_book(self.test_user_id, 2)

        except BookNotBorrowedError as e:
            print("예외 정상 발생 (BookNotBorrowedError):", e)

        except Exception as e:
            print("다른 오류 발생:", e)

    def run_all_tests(self):
        print("\n" + "=" * 30)
        print("   도서 관리 시스템 일괄 테스트 시작")
        print("=" * 30)

        self._prepare_data()
        self._reset_test_state()

        self.test_successful_borrow()
        self.test_successful_return()
        self.test_book_not_found()
        self.test_user_not_found()
        self.test_book_not_available()
        self.test_return_unborrowed_book()

        print("\n" + "=" * 30)
        print("   모든 테스트 완료")
        print("=" * 30)

    def makelogfile(self):
        try:
            self.test_successful_borrow(103, 5)
            self.test_successful_borrow(103, 9)
            self.test_successful_borrow(104, 4)
            self.test_successful_return(103, 5)
            self.test_successful_borrow(103, 10)
            self.test_successful_borrow(104, 5)
            self.test_successful_borrow(105, 2)
            self.test_successful_borrow(105, 3)
            self.test_successful_return(103, 9)
            self.test_successful_return(104, 4)
            self.test_successful_borrow(106, 8)
            self.test_successful_return(103, 9)
            self.test_successful_return(106, 8)
            self.test_successful_borrow(107, 5)
            self.test_successful_borrow(107, 4)
            self.test_successful_return(107, 5)
            self.test_successful_borrow(106, 5)
            self.test_successful_borrow(103, 9)
            self.test_successful_borrow(102, 2)
            self.test_successful_return(103, 9)
            self.test_successful_borrow(106, 8)
            self.test_successful_return(103, 9)
            self.test_successful_borrow(108, 9)

        except UserNotFoundError as e:
            print("예외 정상 발생 (UserNotFoundError):", e)
        except BookNotFoundError as e:
            print("검색 실패:", e)
        except BookNotAvailableError as e:
            print("대여 실패:", e)
        except BookNotBorrowedError as e:
            print("예외 정상 발생 (BookNotBorrowedError):", e)
        except Exception as e:
            print("다른 오류 발생:", e)


class ReportClass:
    def __init__(self, manager, log_filename="library_log.txt"):
        self.manager = manager
        self.log_filename = log_filename

    def _read_logs(self):
        logs = []

        try:
            with open(self.log_filename, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()

                    if not line:
                        continue

                    parts = line.split(",")

                    if len(parts) != 4:
                        continue

                    action, user_id, book_id, log_date = parts

                    logs.append({
                        "action": action,
                        "user_id": int(user_id),
                        "book_id": int(book_id),
                        "date": log_date
                    })

        except FileNotFoundError:
            print(f"경고: {self.log_filename} 파일이 없습니다.")
        except Exception as e:
            print("로그 파일 읽기 오류:", e)

        return logs

    def show_top3_borrowed_books(self, save_file=False, filename="top3_books_report.txt"):
        logs = self._read_logs()

        book_count = {}

        for log in logs:
            if log["action"] == "BORROW":
                book_id = log["book_id"]
                book_count[book_id] = book_count.get(book_id, 0) + 1

        sorted_books = sorted(
            book_count.items(),
            key=lambda item: item[1],
            reverse=True
        )

        report = ""
        report += "\n[도서 대여 TOP 3]\n"
        report += "-" * 30 + "\n"

        if not sorted_books:
            report += "대여 기록이 없습니다.\n"
        else:
            for rank, (book_id, count) in enumerate(sorted_books[:3], start=1):
                try:
                    book = self.manager.find_book_by_id(book_id)
                    report += f"{rank} {book.title}({book_id}) - {count}회\n"
                except BookNotFoundError:
                    report += f"{rank}. 알 수 없는 도서 ID({book_id}) - {count}회\n"
        print(report)

        if save_file:
            self._save_report(report, filename)

    def show_top3_borrow_users(self, save_file=False, filename="top3_users_report.txt"):
        logs = self._read_logs()

        user_count = {}

        for log in logs:
            if log["action"] == "BORROW":
                user_id = log["user_id"]
                user_count[user_id] = user_count.get(user_id, 0) + 1

        sorted_users = sorted(
            user_count.items(),
            key=lambda item: item[1],
            reverse=True
        )

        report = ""
        report += "\n[도서 대여 TOP 3 회원]\n"
        report += "-" * 30 + "\n"

        if not sorted_users:
            report += "대여 기록이 없습니다.\n"
        else:
            for rank, (user_id, count) in enumerate(sorted_users[:3], start=1):
                try:
                    user = self.manager.find_user_by_id(user_id)
                    report += f"{rank}. {user.name} 회원({user_id}) - {count}회\n"

                except UserNotFoundError:
                    report += f"{rank}. 알 수 없는 회원 ID({user_id}) - {count}회\n"

        print(report)

        if save_file:
            self._save_report(report, filename)

    def show_recent5_return_logs(self, save_file=False, filename="recent5_return_report.txt"):
        logs = self._read_logs()

        return_logs = []

        for log in logs:
            if log["action"] == "RETURN":
                return_logs.append(log)

        recent_logs = return_logs[-5:]

        report = ""
        report += "\n[최근 5개 반납 기록]\n"
        report += "-" * 30 + "\n"

        if not recent_logs:
            report += "반납 기록이 없습니다.\n"
        else:
            for index, log in enumerate(reversed(recent_logs), start=1):
                user_id = log["user_id"]
                book_id = log["book_id"]
                log_date = log["date"]

                try:
                    user = self.manager.find_user_by_id(user_id)
                    user_name = user.name
                except UserNotFoundError:
                    user_name = f"알 수 없는 회원({user_id})"

                try:
                    book = self.manager.find_book_by_id(book_id)
                    book_title = book.title
                except BookNotFoundError:
                    book_title = f"알 수 없는 도서({book_id})"

                report += f"{index}. {log_date} / {user_name}({user_id}) / {book_title}({book_id})\n"

        print(report)

        if save_file:
            self._save_report(report, filename)

    def show_all_reports(self, save_file=False, filename="library_total_report.txt"):
        self.show_top3_borrowed_books()
        self.show_top3_borrow_users()
        self.show_recent5_return_logs()

    def _save_report(self, report, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report)

        print(f"{filename} 파일 저장 완료")
