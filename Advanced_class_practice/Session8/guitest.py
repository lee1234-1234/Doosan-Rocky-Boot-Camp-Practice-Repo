import tkinter as tk

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
        self.root.configure(bg=self.bg_color)

        self.create_tab_buttons()
        self.show_rent_return_page()

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

    def make_button(self, parent, text):
        return tk.Button(
            parent,
            text=text,
            font=self.font_normal,
            bg=self.button_blue,
            fg="white",
            relief="solid",
            bd=2
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
            anchor="w"
        )

    def show_rent_return_page(self):
        self.clear_page()
        self.set_tab_style("rent")

        frame = tk.Frame(self.root, bg=self.bg_color)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

        # 공통 배치 기준
        left_x = 55
        right_x = 350
        entry_w = 405
        btn_w = 270
        label_w = 260
        h = 58

        # 1행: 회원 ID 입력 + 조회 버튼
        self.user_id_entry = self.make_entry(frame)
        self.user_id_entry.place(x=left_x, y=40, width=entry_w, height=h)

        user_id_btn = self.make_button(frame, "회원 ID 조회")
        user_id_btn.place(x=470, y=40, width=270, height=h)

        # 2행: 사용자 이름 라벨 + 출력창
        user_name_label = self.make_label(frame, "사용자 이름")
        user_name_label.place(x=left_x, y=130, width=label_w, height=h)

        self.user_name_box = self.make_output_label(frame)
        self.user_name_box.place(x=right_x, y=130, width=entry_w, height=h)

        # 3행: 책 ID 입력 + 조회 버튼
        self.book_id_entry = self.make_entry(frame)
        self.book_id_entry.place(x=left_x, y=220, width=entry_w, height=h)

        book_id_btn = self.make_button(frame, "책 ID 조회")
        book_id_btn.place(x=470, y=220, width=270, height=h)

        # 4행: 책 제목 라벨 + 출력창
        book_title_label = self.make_label(frame, "책 제목")
        book_title_label.place(x=left_x, y=310, width=label_w, height=h)

        self.book_title_box = self.make_output_label(frame)
        self.book_title_box.place(x=right_x, y=310, width=entry_w, height=h)

        # 대여 / 반납 버튼
        rent_btn = self.make_button(frame, "대여")
        rent_btn.place(x=67, y=445, width=340, height=58)

        return_btn = self.make_button(frame, "반납")
        return_btn.place(x=430, y=445, width=340, height=58)

        # 결과 출력 영역
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

        report_btn_w = 448
        report_btn_h = 58
        report_x = 33

        top_book_btn = self.make_button(frame, "도서 대여 TOP 3")
        top_book_btn.place(x=report_x, y=40, width=report_btn_w, height=report_btn_h)

        top_user_btn = self.make_button(frame, "도서 대여 TOP 3 회원")
        top_user_btn.place(x=report_x, y=108, width=report_btn_w, height=report_btn_h)

        recent_return_btn = self.make_button(frame, "최근 3개 반납 기록")
        recent_return_btn.place(x=report_x, y=176, width=report_btn_w, height=report_btn_h)

        self.report_text = tk.Text(
            frame,
            font=self.font_normal,
            bg=self.result_bg,
            relief="solid",
            bd=4
        )
        self.report_text.place(x=47, y=280, width=720, height=520)


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()