class Phone:
    def __init__(self, company, year, color):
        print("휴대폰 생성")
        self.company = company
        self.year = year
        self.color = color

my_phone = Phone("삼성전자", 2005, "Blue")
print(my_phone.company, my_phone.year, my_phone.color)