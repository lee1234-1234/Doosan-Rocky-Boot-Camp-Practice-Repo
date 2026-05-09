# -*- coding: utf-8 -*-
"""
LibraryManagerGUI.py

도서 대여/반납 GUI 파일입니다.
LibraryManagerFunction.py와 같은 폴더에 두고 실행하세요.
"""

import contextlib
import io
import tkinter as tk
from tkinter import messagebox

from LibraryManagerFunction import LibraryManager, TestCase, ReportClass


class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("도서 대여 반납 프로그램")
        self.root.geometry("800x900")
        self.root.resizable(False, False)

        self.bg_color = "#eeeeee"
        self.active_tab = "#dddddd"
        self.inactive_tab = "#888888"
        self.button_blue = "#5aa0d8"
        self.result_bg = "#dcecf8"

        self.font_normal = ("맑은 고딕", 12)
        self.font_tab = ("맑은 고딕", 14)

        self.current_frame = None
        self.result_text = None
        self.report_text = None

        # 조회 성공 여부 확인용 변수
        self.selected_user = None
        self.selected_book = None
        self.is_user_checked = False
        self.is_book_checked = False

        self.root.configure(bg=self.bg_color)

        # GUI 로딩 시 LibraryManager 실행
        #TODO 1

        self.create_tab_buttons()
        self.show_rent_return_page()

        if self.startup_message.strip():
            self.show_message(self.startup_message)

    def load_library_data(self):
        self.library.load_books("books.csv")
        self.library.load_users("users.csv")

    def capture_print(self, func, *args, **kwargs):
        buffer = io.StringIO()

        with contextlib.redirect_stdout(buffer):
            func(*args, **kwargs)

        return buffer.getvalue()

    def capture_call_with_return(self, func, *args, **kwargs):
        buffer = io.StringIO()

        with contextlib.redirect_stdout(buffer):
            return_value = func(*args, **kwargs)

        return {
            "return": return_value,
            "message": buffer.getvalue()
        }

    def show_message(self, message, target="rent", clear=True):
        if target == "report" and self.report_text is not None:
            text_widget = self.report_text
        else:
            text_widget = self.result_text

        if text_widget is None:
            return

        if clear:
            text_widget.delete("1.0", tk.END)

        text_widget.insert(tk.END, message)
        text_widget.see(tk.END)

    def create_tab_buttons(self):
        self.tab_frame = tk.Frame(self.root, bg=self.bg_color)
        self.tab_frame.pack(fill="x")

        self.rent_tab = tk.Button(
            self.tab_frame,
            text="대여 반납",
            font=self.font_tab,
            bg=self.active_tab,
            relief="solid",
            bd=1,
            command=self.show_rent_return_page
        )
        self.rent_tab.place(x=0, y=0, width=400, height=65)

        self.report_tab = tk.Button(
            self.tab_frame,
            text="리포트",
            font=self.font_tab,
            bg=self.inactive_tab,
            relief="solid",
            bd=1,
            command=self.show_report_page
        )
        self.report_tab.place(x=400, y=0, width=400, height=65)

        self.tab_frame.configure(height=70)

    def clear_page(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

    def set_tab_style(self, selected):
        if selected == "rent":
            self.rent_tab.config(bg=self.active_tab)
            self.report_tab.config(bg=self.inactive_tab)
        else:
            self.rent_tab.config(bg=self.inactive_tab)
            self.report_tab.config(bg=self.active_tab)

    def make_button(self, parent, text, command=None):
        return tk.Button(
            parent,
            text=text,
            font=self.font_normal,
            bg=self.button_blue,
            fg="white",
            relief="solid",
            bd=2,
            command=command
        )

    def make_entry(self, parent):
        return tk.Entry(
            parent,
            font=self.font_normal,
            relief="solid",
            bd=3
        )

    def make_label(self, parent, text):
        return tk.Label(
            parent,
            text=text,
            font=self.font_normal,
            bg="#dddddd"
        )

    def make_output_label(self, parent):
        return tk.Label(
            parent,
            text="",
            font=self.font_normal,
            bg=self.result_bg,
            relief="solid",
            bd=3,
            anchor="w",
            padx=10
        )

    def reset_user_check(self, event=None):
        self.selected_user = None
        self.is_user_checked = False

        if hasattr(self, "user_name_box"):
            self.user_name_box.config(text="")

    def reset_book_check(self, event=None):
        self.selected_book = None
        self.is_book_checked = False

        if hasattr(self, "book_title_box"):
            self.book_title_box.config(text="")

    def on_user_search(self):
        user_id = self.user_id_entry.get()

        result = self.capture_call_with_return(
            self.tester.find_user_by_id_for_gui,
            user_id
        )

        user = result["return"]
        message = result["message"]

        if user is not None:
            self.selected_user = user
            self.is_user_checked = True
            self.user_name_box.config(text=user.name)
        else:
            self.selected_user = None
            self.is_user_checked = False
            self.user_name_box.config(text="")

        self.show_message(message, target="rent")

    def on_book_search(self):
        book_id = self.book_id_entry.get()

        result = self.capture_call_with_return(
            self.tester.find_book_by_id_for_gui,
            book_id
        )

        book = result["return"]
        message = result["message"]

        if book is not None:
            self.selected_book = book
            self.is_book_checked = True
            self.book_title_box.config(text=book.title)
        else:
            self.selected_book = None
            self.is_book_checked = False
            self.book_title_box.config(text="")

        self.show_message(message, target="rent")

    def validate_before_rent_or_return(self):
        if not self.is_user_checked or self.selected_user is None:
            messagebox.showwarning("확인 필요", "사용자 id 조회를 먼저 해주세요")
            return False

        if not self.is_book_checked or self.selected_book is None:
            messagebox.showwarning("확인 필요", "책 id 조회를 먼저 해주세요")
            return False

        return True

    def on_borrow(self):
        if not self.validate_before_rent_or_return():
            return

        #TODO 7

        self.show_message(message, target="rent")
        self.refresh_book_title_box_only()

    def on_return(self):
        if not self.validate_before_rent_or_return():
            return

        user_name = self.selected_user.name
        book_title = self.selected_book.title

        confirm = messagebox.askyesno(
            "반납 확인",
            f"{user_name}님 {book_title} 책을 반납하시겠습니까?"
        )

        if not confirm:
            self.show_message("반납 처리를 취소했습니다.", target="rent")
            return

        message = self.capture_print(
            self.tester.return_selected_book_for_gui
        )

        self.show_message(message, target="rent")
        self.refresh_book_title_box_only()

    def refresh_book_title_box_only(self):
        if self.selected_book is None:
            self.book_title_box.config(text="")
            return

        try:
            book = self.library.find_book_by_id(self.selected_book.book_id)
            self.selected_book = book
            self.book_title_box.config(text=book.title)
        except Exception:
            self.selected_book = None
            self.is_book_checked = False
            self.book_title_box.config(text="")

    #TODO 8

    def show_rent_return_page(self):
        self.clear_page()
        self.set_tab_style("rent")

        frame = tk.Frame(self.root, bg=self.bg_color)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

        left_x = 55
        right_x = 350
        entry_w = 405
        label_w = 260
        h = 58

        #TODO 2
        self.user_id_entry.place(x=left_x, y=40, width=entry_w, height=h)
        self.user_id_entry.bind("<KeyRelease>", self.reset_user_check)

        #TODO 3




        user_id_btn.place(x=470, y=40, width=270, height=h)

        user_name_label = self.make_label(frame, "사용자 이름")
        user_name_label.place(x=left_x, y=130, width=label_w, height=h)

        self.user_name_box = self.make_output_label(frame)
        self.user_name_box.place(x=right_x, y=130, width=entry_w, height=h)

        #TODO 4
        self.book_id_entry.place(x=left_x, y=220, width=entry_w, height=h)
        self.book_id_entry.bind("<KeyRelease>", self.reset_book_check)

        #TODO 5

        

        book_id_btn.place(x=470, y=220, width=270, height=h)

        book_title_label = self.make_label(frame, "책 제목")
        book_title_label.place(x=left_x, y=310, width=label_w, height=h)

        self.book_title_box = self.make_output_label(frame)
        self.book_title_box.place(x=right_x, y=310, width=entry_w, height=h)

        rent_btn = self.make_button(
            frame,
            "대여",
            command=self.on_borrow
        )
        rent_btn.place(x=67, y=445, width=340, height=58)

        return_btn = self.make_button(
            frame,
            "반납",
            command=self.on_return
        )
        return_btn.place(x=430, y=445, width=340, height=58)

        self.result_text = tk.Text(
            frame,
            font=self.font_normal,
            bg=self.result_bg,
            relief="solid",
            bd=4
        )
        self.result_text.place(x=67, y=535, width=690, height=260)

    def show_report_page(self):
        self.clear_page()
        self.set_tab_style("report")

        frame = tk.Frame(self.root, bg=self.bg_color)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

        # 첨부 이미지 기준으로 버튼 간격을 넓히고,
        # 하단 결과 박스의 높이는 줄여 배치
        report_btn_w = 448
        report_btn_h = 75
        report_x = 33

        top_book_btn = self.make_button(
            frame,
            "도서 대여 TOP 3",
            command=self.on_report_top_books
        )
        top_book_btn.place(x=report_x, y=40, width=report_btn_w, height=report_btn_h)

        top_user_btn = self.make_button(
            frame,
            "도서 대여 TOP 3 회원",
            command=self.on_report_top_users
        )
        top_user_btn.place(x=report_x, y=150, width=report_btn_w, height=report_btn_h)

        recent_return_btn = self.make_button(
            frame,
            "최근 5개 반납 기록",
            command=self.on_report_recent_returns
        )
        recent_return_btn.place(x=report_x, y=265, width=report_btn_w, height=report_btn_h)

        self.report_text = tk.Text(
            frame,
            font=self.font_normal,
            bg=self.result_bg,
            relief="solid",
            bd=4
        )
        self.report_text.place(x=47, y=420, width=720, height=430)


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()
